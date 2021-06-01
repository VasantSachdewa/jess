from rest_framework import serializers
from scraper.models import Websites


class WebsiteConfigPostValidator(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=100)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=255)

class WebsiteConfigPutValidator(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=False, max_length=100)
    name = serializers.CharField(
        required=False, allow_blank=False, max_length=255)