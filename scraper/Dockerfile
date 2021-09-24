FROM public.ecr.aws/lambda/python:3.8
WORKDIR /app
COPY . /app/
RUN yum -y update && yum -y install gcc
RUN pip install -r requirements.txt
CMD ["scraper.main.sync_vendors"]