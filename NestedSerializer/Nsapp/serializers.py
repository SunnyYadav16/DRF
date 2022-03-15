from .models import CourseModel, InstructorModel
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = InstructorModel
        fields = '__all__'
