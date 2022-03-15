from rest_framework.viewsets import ModelViewSet, generics
from .serializers import CourseSerializer, InstructorSerializer
from .models import InstructorModel, CourseModel


class InstructorView(generics.ListCreateAPIView):
    queryset = InstructorModel.objects.all()
    serializer_class = InstructorSerializer


class CoursesViewList(generics.ListCreateAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer