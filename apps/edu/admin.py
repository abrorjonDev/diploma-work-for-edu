from django.contrib import admin

from edu.models import Course, Teacher, Student, FormRequest


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'price')
    list_filter = ('status',)
    search_fields = ('title',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fish', 'age', 'address')
    search_fields = ('fish', 'address')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('fish', 'contact', 'level', 'tag')
    search_fields = ('fish', 'contact')


@admin.register(FormRequest)
class FormRequestAdmin(admin.ModelAdmin):
    list_display = ('fish', 'phone', )
    search_fields = ('fish', 'phone')