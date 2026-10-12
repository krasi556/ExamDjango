import random

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F, Q
from django.db.models.functions import Length
from django.db.models.lookups import GreaterThan

from core.validators import symbol_validator
from employees.additional import excuses
from employees.managers import EmployeeTopManager


# Create your models here.

class Employee(models.Model):
    objects = EmployeeTopManager()

    class ProfessionChoices(models.TextChoices):
        FULL_STACK_DEVELOPER = 'FULL_STACK_DEV', 'Full-Stack Developer'
        FRONT_END_DEVELOPER = 'FRONT_END_DEV', 'Front-End Developer'
        BACK_END_DEVELOPER = 'BACK_END_DEV', 'Back-End Developer'
        MOBILE_DEVELOPER = 'MOBILE_DEV', 'Mobile App Developer'
        GAME_DEVELOPER = 'GAME_DEV', 'Game Developer'

    is_available = models.BooleanField(default=True)
    current_task = models.CharField(max_length=200, null=True, blank=True)

    first_name = models.CharField(max_length=100,
                                  validators=[symbol_validator])
    last_name = models.CharField(max_length=100,
                                 validators=[symbol_validator])

    @property  # will work to implement  it
    def first_last_name(self):
        return f"{self.first_name} {self.last_name}"

    profession = models.CharField(
        max_length=20,
        choices=ProfessionChoices.choices,
    )
    years_of_experience = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(50),
                    ]
    )
    hourly_rate = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.1)]

    )
    bio = models.TextField()
    photo = models.ImageField(
        upload_to='employees/',
        default='img-def-not-ai.png',
        blank=True,
    )

    skills = models.ManyToManyField(
        to='Skill',
        blank=True,
        related_name='employees'
    )

    class Meta:
        verbose_name_plural = 'Employees'
        constraints = [
            models.CheckConstraint(
                check=~Q(first_name=F('last_name')),
                name='different_first_last_name',
                violation_error_message='Please try something realistic'
            ),
            models.CheckConstraint(
                check=GreaterThan(Length('bio'), 10),
                name='bio_longer_than_10',
                violation_error_message='Give a real  bio'
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.photo:
            self.photo = 'img-def-not-ai.png'

        if not self.is_available:
            if not self.current_task or self.current_task == 'Currently available':
                self.current_task = random.choice(excuses)
        else:
            self.current_task = 'Currently available'
        super().save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=100
                            , unique=True)
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
