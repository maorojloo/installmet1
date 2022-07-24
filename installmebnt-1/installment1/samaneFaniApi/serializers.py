from dataclasses import field
from rest_framework import serializers
from . import models


class CallInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CallInstallment
        fields = '__all__'
