FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app
COPY . /app/

RUN yum -y update && yum -y install gcc
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt


CMD ["/app/worker/runner.worker"]