from django.db import models
from course.models import Course


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    version = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f'{self.course.name}: {self.version}'
