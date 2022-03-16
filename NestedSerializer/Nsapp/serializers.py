from .models import CourseModel, InstructorModel
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='coursemodel-detail')

    class Meta:
        model = InstructorModel
        fields = '__all__'
