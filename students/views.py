from rest_framework.viewsets import ModelViewSet
from students.serializers import StudentSerializer, DetailStudentSerializer, CreateStudentSerializer
from students.models import Student

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = DetailStudentSerializer

    def get_serializer_class(self):
            
            if self.action == 'list' and not self.request.user.is_staff:
                return StudentSerializer
            
            if self.action == 'retrieve' and self.request.user.is_staff:
                return DetailStudentSerializer
            
            if self.request.method == 'POST':
                return CreateStudentSerializer
            
            return StudentSerializer
