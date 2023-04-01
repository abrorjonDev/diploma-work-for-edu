from django.urls import path

from edu.views import (
    CoursesAPIView, CourseAPIView, TeachersAPIView, TeacherAPIView,
    StudentAPIView, StudentsAPIView,
    FormRequestsAPIView, FormRequestDetailAPIView,
    )


urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),

    path('teachers/', TeachersAPIView.as_view(), name='teachers'),
    path('teachers/<int:pk>', TeacherAPIView.as_view(), name='teacher'),

    path('students/', StudentsAPIView.as_view(), name='students'),
    path('students/<int:pk>', StudentAPIView.as_view(), name='student'),

    path('forms/', FormRequestsAPIView.as_view(), name='forms'),
    path('forms/<int:pk>', FormRequestDetailAPIView.as_view(), name='form'),
]