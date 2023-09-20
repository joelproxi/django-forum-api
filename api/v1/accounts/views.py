from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAdminUser

from api.v1.accounts.models import CustomUser
from api.v1.accounts.serializers import CustomUserSerializer
# Create your views here.

class RegisterUserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    
class UsersViewset(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset =  CustomUser.objects.all()
    permission_classes = [IsAdminUser]
    

class RetriveUserData(RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    
    def get_object(self):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user
    
    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        data = serializer.data
        return Response(data=data)
    