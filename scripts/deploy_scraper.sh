#!/bin/bash
docker build -t scraper -f scraper/Dockerfile .
docker tag scraper:latest 640734209900.dkr.ecr.ap-southeast-1.amazonaws.com/scraper:latest
docker push 640734209900.dkr.ecr.ap-southeast-1.amazonaws.com/scraper:latest
