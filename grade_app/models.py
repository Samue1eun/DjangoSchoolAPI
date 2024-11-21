from django.db import models
from django.core import validators
from student_app.models import Student
from subject_app.models import Subject

# Grade Model
class Grade(models.Model):
    grade = models.DecimalField(unique = False, null=False, default = 100, max_digits=5, decimal_places=2)
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)