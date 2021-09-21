import datetime
import logging as logger
from functools import wraps
from typing import Callable
from jess.exceptions import MetricException

import boto3
from jess.settings import CLOUDWATCH_NAMESPACE


CLOUDWATCH_CLIENT = boto3.client('cloudwatch')


def counter(metric_name: str) -> Callable:
    
    def wrapper(func: Callable) -> Callable:
        
        @wraps(func)
        def implementation(*args, **kwargs):
            output = func(*args, **kwargs)
            _counter()

            return output
            
        def _counter():
            try:
                response = CLOUDWATCH_CLIENT.put_metric_data(
                    MetricData = [
                        {
                            'MetricName': metric_name,
                            'Value': 1,
                            'StorageResolution': 1,
                            'Timestamp': datetime.datetime.now(datetime.timezone.utc)
                        },
                    ],
                    Namespace=CLOUDWATCH_NAMESPACE
                )
            except Exception as e:
                raise MetricException(e)
            except MetricException:
                pass  
            
        return implementation 
            
    return wrapper
