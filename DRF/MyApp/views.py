from django.http import JsonResponse
# from django.shortcuts import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializers = EmployeeSerializer(employees, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        # json_data = JSONParser().parse(request)
        """ Parses the incoming bytestream as JSON and returns the resulting data. """
        serializers = EmployeeSerializer(data=request.data)  # This is for deserializing

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetailView(request, pk):
    try:
        emp = Employee.objects.get(id=pk)

        if request.method == 'DELETE':
            emp.delete()
            return Response(status=status.HTTP_410_GONE)

        elif request.method == 'GET':
            serializers = EmployeeSerializer(emp)
            return Response(serializers.data)

        elif request.method == 'PUT':
            # json_data = JSONParser().parse(request)
            serializers = EmployeeSerializer(emp, data=request.data)

            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)

    except Employee.DoesNotExist:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def userListView(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)
