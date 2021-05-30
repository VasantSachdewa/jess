from django.db import models
from typing import Dict
import json

# Create your models here.
class Websites(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def to_dict(self) ->  Dict:
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }
