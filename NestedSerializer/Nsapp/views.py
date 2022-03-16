from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, generics
from .serializers import CourseSerializer, InstructorSerializer
from .models import InstructorModel, CourseModel
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

users = User.objects.all()

for user in users:
    token = Token.objects.get_or_create(user=user)


class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        # return super().has_permission(request, view)
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True

        return False


class InstructorView(generics.ListCreateAPIView):
    queryset = InstructorModel.objects.all()
    serializer_class = InstructorSerializer


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstructorModel.objects.all()
    serializer_class = InstructorSerializer


class CoursesViewList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
