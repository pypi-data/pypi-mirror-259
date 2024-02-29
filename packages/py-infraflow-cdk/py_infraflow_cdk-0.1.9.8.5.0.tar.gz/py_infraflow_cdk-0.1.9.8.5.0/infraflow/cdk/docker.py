import copy
from datetime import timedelta
from typing import Union

from aws_cdk import aws_ecs as ecs, Duration
from aws_cdk import aws_ecs_patterns as ecs_patterns
from aws_cdk import aws_ecr_assets as assets
from aws_cdk.aws_ec2 import SubnetSelection, SubnetType, Subnet, SubnetFilter
from aws_cdk.aws_applicationautoscaling import ScalingInterval, Schedule
from aws_cdk import aws_sqs as sqs
from aws_cdk.aws_ecs import Cluster, FargatePlatformVersion

from infraflow.cdk import ServiceStageStack
from infraflow.cdk.core.utils import to_duration
from infraflow.cdk.sg.patterns import SecurityGroupTarget


class ContainerSize:
    def __init__(self, cpu: int = 256, memory_limit_mib: int = 512):
        self.memory_limit_mib = memory_limit_mib
        self.cpu = cpu


class ContainerImage:
    def __init__(
            self,
            path=None,
            ecr_image=None,
    ):
        self.ecr_image = ecr_image
        self.path = path


class ContainerInstanceInfo:
    def __init__(
            self,
            image: ContainerImage,
            command: str = None,
            count=1,
            max_count=1,
            size: ContainerSize = ContainerSize(),
            environment: dict[str, str] = {}
    ):
        self.image = image
        self.command = command
        self.count = count
        self.size = size
        self.environment = environment
        self.max_count = max_count


class EcsCluster:
    def __init__(self, scope: ServiceStageStack, cluster_name: str, subnet_type: SubnetType = SubnetType.PRIVATE_WITH_EGRESS):
        self.subnet_type = subnet_type
        self.scope = scope
        vpc = self.scope.env.vpc

        self.cluster = ecs.Cluster(self.scope, cluster_name, vpc=vpc)

    def get_image(self, image: ContainerImage, name):
        if image.path:
            image_asset = assets.DockerImageAsset(self.scope, f"{name}_image", directory=image.path)
            local_image = ecs.ContainerImage.from_docker_image_asset(image_asset)
        else:
            local_image = None
        cdk_image = ecs.ContainerImage.from_registry(
            image.ecr_image) if image.ecr_image else local_image if image.path else None
        return cdk_image

    def subnets(self):
        subnets = self.scope.env.service_subnets(self.subnet_type)
        print("*** docker subnets for ApplicationLoadBalancedFargateService")
        for subnet in subnets:
            print("*** docker subnet_id:", subnet.subnet_id)
        return SubnetSelection(subnets=subnets)

    def get_security_group(self, name):
        return self.scope.security_groups.get_group(target=SecurityGroupTarget(
            self.cluster,
            id=name + 'SG',
            cdk_type=Cluster,
            infraflow_pattern=self,
        ))

    def load_balanced_service(
            self,
            name,
            container: ContainerInstanceInfo
    ):
        environment = {**self.scope.env.environment_vars, **container.environment}
        return ecs_patterns.ApplicationLoadBalancedFargateService(
            self.scope, f"{name}_service",
            cluster=self.cluster,  # Required
            cpu=container.size.cpu,  # Default is 256
            desired_count=container.count,  # Default is 1
            listener_port=80,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=self.get_image(image=container.image, name=name),
                container_name=f"{name}_task",
                container_port=80,
                environment=environment,
                command=container.command,
                ## taskRole= IMPLEMENT!
            ),
            security_groups=[self.get_security_group(name)],
            task_subnets=self.subnets(),
            assign_public_ip=False,
            public_load_balancer=False,
            memory_limit_mib=container.size.memory_limit_mib,  # Default is 512
        )  # Default is True

    def queued_service(
            self,
            name,
            container: ContainerInstanceInfo,
            queue: sqs.Queue
            , max_receive_count=None, visibility_timeout=None, scaling_steps: list[ScalingInterval] = None):
        environment = {**self.scope.env.environment_vars, **container.environment}
        return ecs_patterns.QueueProcessingFargateService(
            self.scope, f"{name}_service",
            cluster=self.cluster,  # Required
            cpu=container.size.cpu,  # Default is 256
            min_scaling_capacity=container.count,
            max_scaling_capacity=container.max_count,
            max_receive_count=max_receive_count,
            visibility_timeout=visibility_timeout,
            scaling_steps=scaling_steps,
            image=self.get_image(image=container.image, name=name),
            environment=environment,
            command=container.command,
            queue=queue,
            security_groups=[self.get_security_group(name)],
            task_subnets=self.subnets(),
            assign_public_ip=False,
            memory_limit_mib=container.size.memory_limit_mib,  # Default is 512
        )  # Default is True

    def scheduled_service(
            self,
            name,
            container: ContainerInstanceInfo,
            schedule: Union[Duration, timedelta, int]
    ):
        environment = {**self.scope.env.environment_vars, **container.environment}
        return ecs_patterns.ScheduledFargateTask(
            self.scope, f"{name}_service",
            cluster=self.cluster,  # Required
            cpu=container.size.cpu,  # Default is 256
            desired_task_count=container.count,
            scheduled_fargate_task_image_options=ecs_patterns.ScheduledFargateTaskImageOptions(
                image=self.get_image(image=container.image, name=name),
                container_name=f"{name}_task",
                container_port=80,
                environment=environment,
                command=container.command
            ),
            schedule=Schedule.rate(duration=to_duration(schedule)),
            subnet_selection=self.subnets(),
            security_groups=[self.get_security_group(name)],
            memory_limit_mib=container.size.memory_limit_mib,  # Default is 512
        )  # Default is True



def add_queue_environment_variables(
        environment: dict[str, str],
        queue,
        retry=None,
        dlq=None
) -> dict[str, str]:
    environment = copy.copy(environment)
    environment['SQS_QUEUE'] = retry
    environment['SQS_RETRY_QUEUE'] = retry
    environment['SQS_DEAD_LETTER_QUEUE'] = dlq
    return environment