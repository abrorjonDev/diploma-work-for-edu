from django.contrib import admin

from stats.models import Income, Outcome

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'value', 'month', 'year')


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'month', 'year')