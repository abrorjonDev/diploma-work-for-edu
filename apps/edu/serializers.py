from rest_framework import serializers
from django.forms import model_to_dict

from edu.models import Course, Teacher, Student, FormRequest


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


class FormRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormRequest
        fields = "__all__"
        read_only_fields = ('is_seen',)


class FormRequestSeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormRequest
        fields = ('is_seen',)
