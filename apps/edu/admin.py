from django.contrib import admin

from edu.models import Course, Teacher, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
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