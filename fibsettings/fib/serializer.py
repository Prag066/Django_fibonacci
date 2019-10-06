from rest_framework import serializers
from .models import Fib_data 
from django.contrib.auth.models import User

class FibSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fib_data
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'