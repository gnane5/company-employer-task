from rest_framework import serializers
from .models import *



class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password', 'created_at']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password', 'employer', 'created_at']
        read_only_fields = ['employer']


class TaskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Task
        fields = ['id', 'assigned_to', 'employer', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['employer']


