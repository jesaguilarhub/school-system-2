from rest_framework.viewsets import ModelViewSet
from instructors.serializers import InstructorSerializer, DetailInstructorSerializer, CreateInstructorSerializer
from instructors.models import Instructor

class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = DetailInstructorSerializer

    def get_serializer_class(self):
            
            if self.action == 'list' and not self.request.user.is_staff:
                return InstructorSerializer
            
            if self.action == 'retrieve' and self.request.user.is_staff:
                return DetailInstructorSerializer
            
            if self.request.method == 'POST':
                return CreateInstructorSerializer
            
            return InstructorSerializer
