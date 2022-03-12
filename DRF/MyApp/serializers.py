from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['id', 'name', 'email', 'password', 'phone']
        fields = '__all__'

    """When we use only serializer.Serializer, we need to write the fields and the operations on it like this."""
    # name = serializers.CharField(max_length=50)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=50)
    # phone = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)  # We use ** symbol here to pass a dictionary as a data
    #
    # def update(self, emp, validated_data):
    #     new_emp_data = Employee(**validated_data)
    #     new_emp_data.id = emp.id
    #     new_emp_data.save()
    #     return new_emp_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password']
        fields = '__all__'

    # username = serializers.CharField(max_length=50)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=50)
