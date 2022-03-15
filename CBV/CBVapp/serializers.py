from rest_framework import serializers
from .models import CBVCourse


class CBVCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBVCourse
        fields = '__all__'
