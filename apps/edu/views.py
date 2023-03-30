from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from edu.models import Course, Teacher, Student
from edu.serializers import CourseSerializer, TeacherSerializer, StudentSerializer


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