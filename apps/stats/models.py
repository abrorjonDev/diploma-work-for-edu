from django.db import models
from django.utils import timezone
from stats.consts import MONTH, YEARS


class BaseModel(models.Model):
    month = models.PositiveIntegerField(choices=MONTH, default=timezone.now().month)
    year = models.PositiveIntegerField(choices=YEARS, default=timezone.now().year)
    comment = models.CharField(max_length=300, default="")
    value = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Income(BaseModel):
    student = models.ForeignKey("edu.Student", models.CASCADE, related_name='payments')
    course = models.ForeignKey("edu.Course", models.CASCADE, related_name='courses')
    
    def __str__(self):
        return str(self.student)


class Outcome(BaseModel):
    ...
