from django.urls import path
from .views import *

urlpatterns = [

    path('employers/', EmployerListView.as_view(), name='employer-list'),
    path('employers/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),
    path('employers/login/', EmployerLogin.as_view(), name='employer-login'),

    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/login/', EmployeeLogin.as_view(), name='employer-login'),

    path('employer/tasks/', TaskEmployerListCreateView.as_view(), name='employer-task-list-create'),
    path('employer/tasks/<int:pk>/', TaskEmployerDetailView.as_view(), name='employer-task-detail'),

    path('employee/tasks/', TaskEmployeeListCreateView.as_view(), name='employee-task-list'),
    path('employee/tasks/<int:pk>/', TaskEmployeeDetailView.as_view(), name='employee-task-detail'),
]