from django.urls import path
from .views import InstructorView, CoursesViewList, CoursesDetailView, InstructorDetailView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('list/', InstructorView.as_view(), name='instructor_list'),
    path('courselist/', CoursesViewList.as_view(), name='course_list'),
    path('courselist/<int:pk>', CoursesDetailView.as_view(), name='coursemodel-detail'),
    path('instructorlist/<int:pk>', InstructorDetailView.as_view(), name='instructormodel-detail'),
    path('auth/login/', TokenObtainPairView.as_view(), name='create-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
