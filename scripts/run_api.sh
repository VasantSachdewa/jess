#!/bin/bash
docker run --env-file .env -d -p8001:8001 job_scanner_api uwsgi --http :8001 --wsgi-file jess/wsgi.py