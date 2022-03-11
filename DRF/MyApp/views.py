from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializers = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif request.method == 'POST':
        json_data = JSONParser().parse(request)
        """ Parses the incoming bytestream as JSON and returns the resulting data. """
        print(json_data)
        serializers = EmployeeSerializer(data=json_data)  # This is for deserializing

        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse(serializers.errors, safe=False)


def userListView(request):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return JsonResponse(serializers.data, safe=False)
