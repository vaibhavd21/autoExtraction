from dataclasses import fields
from rest_framework_json_api import serializers
from .models import data

class dataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields = ('host','product','startDate','endDate','request_at')