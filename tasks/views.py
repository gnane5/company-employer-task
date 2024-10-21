from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied
from .models import *
from .serializers import *
from .backends import *


class EmployerListView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerLogin(generics.CreateAPIView):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not phone_number:
            return Response({'error': 'Provide either phone_number'}, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            return Response({'error': 'Provide password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        if phone_number:
            user = Employer.objects.filter(phone_number=phone_number).first()

        if not user:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        if not password == user.password:
            return Response({'error': 'Invalid password.'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'refresh_token': refresh_token,
            'access_token': access_token
        }, status=status.HTTP_200_OK)



class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    authentication_classes = [EmployerUserJWTAuthentication]

    def get_queryset(self):
        return Employee.objects.filter(employer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    authentication_classes = [EmployerUserJWTAuthentication]

    def get_queryset(self):
        return Employee.objects.filter(employer=self.request.user)


class EmployeeLogin(generics.CreateAPIView):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not phone_number:
            return Response({'error': 'Provide either phone_number'}, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            return Response({'error': 'Provide password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        if phone_number:
            user = Employee.objects.filter(phone_number=phone_number).first()

        if not user:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        if not password == user.password:
            return Response({'error': 'Invalid password.'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'refresh_token': refresh_token,
            'access_token': access_token
        }, status=status.HTTP_200_OK)




class TaskEmployerListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [EmployerUserJWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(employer=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


class TaskEmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [EmployerUserJWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(employer=self.request.user.id)


class TaskEmployeeListCreateView(generics.ListAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [EmployeeUserJWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user.id)


class TaskEmployeeDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [EmployeeUserJWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user.id)