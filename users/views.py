from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from users.serializers import DetailUserSerializer, CreateUserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from users.tasks import send_email
from datetime import datetime, timedelta

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = DetailUserSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serialized  = serializer(data=self.request.data)

        if not serialized.is_valid():
            return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serialized.errors
            )

        serialized.save()
        
        send_email_datetime = datetime.now() + timedelta(seconds=20)
        send_email.apply_async(eta=send_email_datetime)
        
        return Response(
            status=status.HTTP_201_CREATED,
            data=serialized.data
        )

    def get_serializer_class(self):
                       
            if self.action == 'retrieve' and self.request.user.is_staff:
                return DetailUserSerializer
            
            if self.request.method == 'POST':
                return CreateUserSerializer
            
        
    
