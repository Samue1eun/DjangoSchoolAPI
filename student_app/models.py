from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_name_format
from .validators import validate_combination_format
from .validators import validate_school_email
from .validators import subject_limit
from .validators import grade_limit
from .validators import decimal_limit

# Create your models here.

# Subject model
class Subject(models.Model):
    subject_name = models.CharField(unique=True, null=False)
    professor = models.CharField(unique=False, default="Mr.Cahan", null=False)
    student = models.ManyToManyField('Student')

# Student model
class Student(models.Model):
    name = models.CharField(unique=False, null=False, validators=[validate_name_format])
    student_email =models.EmailField(unique=True, null=False, validators=[validate_school_email])
    personal_email =models.EmailField(unique=True, null=True)
    locker_number = models.IntegerField(unique=True, default=110, null=False, validators=[MinValueValidator(1), MaxValueValidator(200)])
    locker_combination = models.CharField(unique=False, default="12-12-12", null=False,  validators=[validate_combination_format])
    good_student = models.BooleanField(unique=False, default=True, blank=True)
    subjects = models.ManyToManyField(Subject, validators=[subject_limit])

# Grade Model
class Grade(models.Model):
    grade = models.DecimalField(unique = False, null=False, default = 100, max_digits=2,)

# Model methods

# String method
def __str__(self):
    return f"{self.name} - {self.student_email} - {self.locker_number}"

# Add Subject method

# Remove Subject method