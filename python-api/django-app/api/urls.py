from django.urls import path
from .views import get_users, create_user, get_health, get_employees, get_employee, create_employee

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('health/', get_health, name='get_health'),
    path('employees/', get_employees, name='get_employees'),
    path('employees/<int:id>/', get_employee, name='get_employee'),
    path('employees/create/', create_employee, name='create_employee'),
]