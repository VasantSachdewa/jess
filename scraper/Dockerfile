FROM python:3.9
WORKDIR /app
COPY . /app/
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev
RUN pip install -r requirements.txt
RUN python -m pip install awslambdaric
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
COPY scripts/run_scraper.sh /app
RUN chmod 755 /usr/bin/aws-lambda-rie /app/run_scraper.sh
CMD ["sh", "run_scraper.sh"]