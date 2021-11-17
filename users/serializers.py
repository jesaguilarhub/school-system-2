from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class DetailUserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class CreateUserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_superuser', 'is_staff']