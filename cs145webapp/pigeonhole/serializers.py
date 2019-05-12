from rest_framework import serializers
from .models import PigeonholeAction

class PigeonholeActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = PigeonholeAction
		fields = ('id_number', 'name', 'p_number', 'timestamp')
	