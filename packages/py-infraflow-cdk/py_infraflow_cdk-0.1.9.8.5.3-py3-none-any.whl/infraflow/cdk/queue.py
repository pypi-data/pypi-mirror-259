from datetime import timedelta
from typing import Union
from aws_cdk import Duration

from infraflow.cdk.core.utils import to_duration


class QueueSubscription:
    def __init__(self, max_receive_count: int = 1, timeout: Union[Duration, timedelta, int] = 30):
        self.max_receive_count: int = max_receive_count
        self.timeout: Duration = to_duration(timeout)