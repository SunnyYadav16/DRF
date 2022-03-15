from django.urls import path
from .views import InstructorView, CoursesViewList

urlpatterns = [
    path('list/', InstructorView.as_view(), name='instructor_list'),
    path('courselist/', CoursesViewList.as_view(), name='course_list'),
]
