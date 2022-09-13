from .models import Plan
from rest_framework import serializers


class PlansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = "__all__"