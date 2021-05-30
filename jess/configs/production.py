import os

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'job_scanner'),
        'USER': os.getenv('DB_USERNAME', 'donthardcode'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'donthardcode'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432')
    }
}