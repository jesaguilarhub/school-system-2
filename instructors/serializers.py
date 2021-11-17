from rest_framework.serializers import ModelSerializer
from instructors.models import Instructor

class InstructorSerializer(ModelSerializer):

    class Meta:
        model = Instructor
        fields = ['id', 'name']

class DetailInstructorSerializer(ModelSerializer):
    
    class Meta:
        model = Instructor
        fields = '__all__'

class CreateInstructorSerializer(ModelSerializer):
    
    class Meta:
        model = Instructor
        fields = '__all__'