from django.core.exceptions import ValidationError
import re

# Name Validator

def validate_name_format(value):
    if not re.match(r'^[A-Za-z]+ [A-Z]\. [A-Za-z]+$', value):
        raise ValidationError(
            'Name must be in the format "First Middle Initial. Last"'
        )

# School Email Validator

def validate_school_email(value):
    if not re.match(r'^[A-Za-z]+[0-9]*@school.com$', value):
        raise ValidationError(
            'Invalid school email format. Please use an email ending with "@school.com".'
            )
    
# Personal Email Validator

def validate_combination_format(value):
    if not re.match(r'^\d{2}-\d{2}-\d{2}$', value):
        raise ValidationError(
            'Combination must be in the format "12-12-12"'
        )

# Subject Validator

def subject_limit(value):
    if value > 8:
        raise ValidationError(
            "This students class schedule is full!"
        )
    if value < 1:
        raise ValidationError(
            "This students class schedule is empty!"
        )
    
# Grade Validator

def grade_limit(value):
    if value > 100:
        raise ValidationError(
            "Ensure this value is less than or equal to 100.0."
        )
    if value < 0:
        raise ValidationError(
            "Ensure this value is greater than or equal to 0.0."
        )

# Decimal Validator

def decimal_limit(value):
    if not re.match(r'^\d+(\.\d{1,3})?$', value):
        raise ValidationError(
            "numeric field overflow"
        )