from django.db import models

from core.validators import symbol_validator
from employees.models import Employee


# Create your models here.

class Application(models.Model):
    first_name = models.CharField(max_length=100,
                                  validators=[symbol_validator])
    last_name = models.CharField(max_length=100,
                                 validators=[symbol_validator])
    email = models.EmailField()
    desired_position = models.CharField(
        max_length=20,
        choices=Employee.ProfessionChoices.choices,
        )
