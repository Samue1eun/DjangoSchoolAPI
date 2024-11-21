from django.db import models
from django.core import validators

# Grade Model
class Grade(models.Model):
    grade = models.DecimalField(unique = False, null=False, default = 100, max_digits=5, decimal_places=2)