from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_name_format
from .validators import validate_combination_format
from .validators import validate_school_email
from .validators import subject_limit
from .validators import grade_limit
from .validators import decimal_limit
# from subject_app.models import Subject

# Create your models here.

# Student model
class Student(models.Model):
    name = models.CharField(unique=False, null=False, validators=[validate_name_format])
    student_email =models.EmailField(unique=True, null=False, validators=[validate_school_email])
    personal_email =models.EmailField(unique=True, null=True)
    locker_number = models.IntegerField(unique=True, default=110, null=False, validators=[MinValueValidator(1), MaxValueValidator(200)])
    locker_combination = models.CharField(unique=False, default="12-12-12", null=False,  validators=[validate_combination_format])
    good_student = models.BooleanField(unique=False, default=True, blank=True)
    # subjects = models.ManyToManyField('subject_app.Subject')

# Model methods

# String method
def __str__(self):
    return f"{self.name} - {self.student_email} - {self.locker_number}"

# Add Subject method

# Remove Subject method