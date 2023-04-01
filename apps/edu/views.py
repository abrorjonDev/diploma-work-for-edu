from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.exceptions import NotAuthenticated
from drf_yasg.utils import swagger_auto_schema

from edu.models import Course, Teacher, Student, FormRequest
from edu.serializers import (
    CourseSerializer, 
    TeacherSerializer,
    StudentSerializer, 
    FormRequestSerializer, FormRequestSeenSerializer,
    )


class CoursesAPIView(ListCreateAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseAPIView(RetrieveUpdateDestroyAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeachersAPIView(ListCreateAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = Teacher.objects.prefetch_related('course_set')
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeacherAPIView(RetrieveUpdateDestroyAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = Teacher.objects.prefetch_related('course_set')
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentsAPIView(ListCreateAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = Student.objects.prefetch_related('courses')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentAPIView(RetrieveUpdateDestroyAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = Student.objects.prefetch_related('courses')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FormRequestsAPIView(ListCreateAPIView):
    """Authenticated users can get requests while others post only."""

    queryset = FormRequest.objects.prefetch_related('courses')
    serializer_class = FormRequestSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.is_seen is None:
            return qs
        return qs.filter(is_seen=self.is_seen)

    @swagger_auto_schema(query_serializer=FormRequestSeenSerializer)
    def get(self, request):
        if request.user.is_anonymous:
            raise NotAuthenticated()
        self.is_seen = request.query_params.get('is_seen', None)
        return super().get(request)


class FormRequestDetailAPIView(RetrieveUpdateDestroyAPIView):
    """Authenticated users can post requests while others get only."""

    queryset = FormRequest.objects.prefetch_related('courses')
    serializer_class = FormRequestSerializer
    edit_serializer_class = FormRequestSeenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['get']:
            return super().get_serializer_class()
        return self.edit_serializer_class