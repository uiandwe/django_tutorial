from rest_framework import serializers
from .models import Lotte


class LotteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lotte
        fields = '__all__'
