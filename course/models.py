from django.db import models
from django.core.cache import cache


class Course(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def get_course_version_key(self):
        return f'{self.id}-version'

    def get_current_version(self):
        return cache.get(self.get_course_version_key())

    def get_current_questions(self):
        version = self.get_current_version()
        return self.question_set.get(version=version) if version else None
