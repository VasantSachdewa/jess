FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["/app/worker/runner.worker"]