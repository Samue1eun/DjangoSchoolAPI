from django.db import models
from django.core import validators
from student_app.models import Student
from .validators import validate_subject_format, validate_professor_name

# Subject model
class Subject(models.Model):
    subject_name = models.CharField(unique=True, null=False, validators=[validate_subject_format])
    professor = models.CharField(unique=False, default="Mr. Cahan", null=False, validators=[validate_professor_name])
    students = models.ManyToManyField(Student, related_name="subjects")

# Class Methods

def __str__(self):
    return f"{self.subject_name} - {self.professor}-{self.student.count()}"

# Add Student method

def add_student(self, student):
    self.student.add(student)
    self.save()

# Remove Student method

def remove_student(self, student):
    self.student.remove(student)
    self.save()