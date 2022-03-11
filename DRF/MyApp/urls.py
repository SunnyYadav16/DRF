from django.urls import path
from .views import employeeListView, userListView

urlpatterns = [
    path('emplist/', employeeListView, name="emplist"),
    path('userlist/', userListView, name="userlist"),
]
