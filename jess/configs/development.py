import os

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "job_scanner"),
        "USER": os.getenv("DB_USERNAME", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", "bangbang"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# Kafka Configuration
KAFKA_CONFIG = {
    "KAFKA_HOST": [os.getenv("KAFKA_HOST", "kafka:9092")],
    "KAFKA_TOPIC": os.getenv("KAFKA_TOPIC", "new_jobs"),
}

#Cloudwatch Configuration
CLOUDWATCH_NAMESPACE = os.getenv("CLOUDWATCH_NAMESPACE", "development")
