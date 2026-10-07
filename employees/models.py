import random

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.templatetags.static import static

from core.validators import symbol_validator
from employees.additional import excuses


# Create your models here.

class Employee(models.Model):
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

    def __str__(self):
        return self.name
