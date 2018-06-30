from django.db import models


class Course(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name
