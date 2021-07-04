from django.db import models
from typing import Dict
import json

# Create your models here.
class Websites(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    url = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> Dict:
        return {"id": self.id, "name": self.name, "url": self.url}
