from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CBVCourse
from django.http import Http404
from .serializers import CBVCourseSerializer
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet


class CourseListView(ModelViewSet):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer


"""
class CourseListView(ViewSet):
    def list(self, request):
        courses = CBVCourse.objects.all()
        serializers = CBVCourseSerializer(courses, many=True)
        return Response(serializers.data)

    def create(self, request):
        serializers = CBVCourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

    def retrieve(self, request, pk):
        try:
            course = CBVCourse.objects.get(id=pk)
        except course.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializers = CBVCourseSerializer(course)
        return Response(serializers.data)
"""

"""
class CourseListView(generics.ListCreateAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer
"""

"""class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer
"""

"""class CourseDetailView(generics.RetrieveUpdateAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer
"""

"""
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer


class CourseDetailView(generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer
"""

"""
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
"""

"""
class CourseDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = CBVCourse.objects.all()
    serializer_class = CBVCourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

"""
class CourseListView(APIView):
    def get(self, request):
        course_list = CBVCourse.objects.all()
        serializer = CBVCourseSerializer(course_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        courseserializer = CBVCourseSerializer(data=request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(courseserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get_course(self, pk):
        try:
            course_detail_view = CBVCourse.objects.get(id=pk)
            return course_detail_view

        except CBVCourse.DoesNotExist:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            raise Http404

    def get(self, request, pk):
        my_course = self.get_course(pk)
        serializer = CBVCourseSerializer(my_course)
        return Response(serializer.data)

    def put(self, request, pk):
        my_course = self.get_course(pk)
        serializer = CBVCourseSerializer(instance=my_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        my_course = self.get_course(pk)
        my_course.delete()
        return Response(status=status.HTTP_410_GONE)
"""
