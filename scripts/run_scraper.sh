#!/bin/bash
export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=jess.settings
python manage.py migrate
python scraper/main.py