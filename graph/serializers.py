from collections import OrderedDict
from django.forms import widgets
from rest_framework import serializers
from models import HouseholdResult
import json


class HouseholdResultSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    result = serializers.CharField(max_length=30,read_only=True)

    class Meta:
        model = HouseholdResult
        fields = []

    def update(self, instance, validated_data):
        if instance:
            instance.result = validated_data.get('result', instance.result)
            instance.id = validated_data.get('id', instance.id)
            instance.save()
            return instance
        return HouseholdResult(**attrs)

    def create(self, validated_data):
        return HouseholdResult.objects.create(**validated_data)

    def to_representation(self, instance):
        if instance:
           ret = super(HouseholdResultSerializer, self).to_representation(self)
           ret['id']= instance.id
           ret['result']= instance.result
           return ret

