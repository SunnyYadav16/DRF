from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import CourseModel
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def courseview(request):
    if request.method == 'GET':
        course_list = CourseModel.objects.all()
        serializer = CourseSerializer(course_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def courseDetailView(request, pk):

    try:
        course_detail_view = CourseModel.objects.get(id=pk)

        if request.method == 'GET':
            serializer = CourseSerializer(course_detail_view)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CourseSerializer(course_detail_view, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

        elif request.method == 'DELETE':
            course_detail_view.delete()
            return Response(status=status.HTTP_410_GONE)

    except CourseModel.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


