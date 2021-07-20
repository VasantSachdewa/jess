#!/bin/sh
MODULE="scraper.main.sync_vendors"
python manage.py migrate
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec /usr/bin/aws-lambda-rie /usr/local/bin/python -m awslambdaric $MODULE
else
    exec /usr/local/bin/python -m awslambdaric $MODULE
fi