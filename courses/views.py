from rest_framework.viewsets import ModelViewSet
from courses.serializers import CourseSerializer, DetailCourseSerializer, CreateCourseSerializer
from courses.models import Course

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = DetailCourseSerializer

    def get_serializer_class(self):
            
            if self.action == 'list' and not self.request.user.is_staff:
                return CourseSerializer
            
            if self.action == 'retrieve' and self.request.user.is_staff:
                return DetailCourseSerializer
            
            if self.request.method == 'POST':
                return CreateCourseSerializer
            
            return CourseSerializer