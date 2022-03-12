from django.urls import path
from .views import employeeListView, userListView, employeeDetailView

urlpatterns = [
    path('emplist/', employeeListView, name="emplist"),
    path('userlist/', userListView, name="userlist"),
    path('employee/<int:pk>', employeeDetailView , name="empDetailView"),
]
