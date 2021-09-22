import datetime
import logging as logger
from functools import wraps
from typing import Callable
from jess.exceptions import MetricException

import boto3
import time
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


def timer(metric_name: str) -> Callable:
    
    def wrapper(func: Callable) -> Callable:
        
        @wraps(func)
        def implementation(*args, **kwargs):
            time1 = time.time()
            output = func(*args, **kwargs)
            time2 = time.time()
            elasped_time = round((time2 - time1)*1000, 3)
            _timer(elasped_time)

            return output
            
        def _timer(elasped_time: float):
            try:
                response = CLOUDWATCH_CLIENT.put_metric_data(
                    MetricData = [
                        {
                            'MetricName': '{}-{}'.format(metric_name, 'timer'),
                            'Value': elasped_time,
                            'StorageResolution': 1,
                            'Timestamp': datetime.datetime.now(datetime.timezone.utc),
                            'Unit': 'Milliseconds'
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
