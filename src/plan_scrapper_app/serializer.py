from .models import Plans
from rest_framework import serializers


class PlansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plans
        fields = "__all__"