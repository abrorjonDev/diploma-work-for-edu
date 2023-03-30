from rest_framework import serializers
from django.forms import model_to_dict

from edu.models import Course, Teacher, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.teacher:
            data['teacher'] = model_to_dict(instance.teacher, ('id', 'fish', 'level'))
        return data


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['courses'] = instance.course_set.values('id', 'title', 'status')
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['courses'] = instance.courses.values('id', 'title', 'status')
        return data