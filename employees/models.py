from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Employee(models.Model):
    class ProfessionChoices(models.TextChoices):
        FULL_STACK_DEVELOPER = 'FULL_STACK_DEV', 'Full-Stack Developer'
        FRONT_END_DEVELOPER = 'FRONT_END_DEV', 'Front-End Developer'
        BACK_END_DEVELOPER = 'BACK_END_DEV', 'Back-End Developer'
        MOBILE_DEVELOPER = 'MOBILE_DEV', 'Mobile App Developer'
        GAME_DEVELOPER = 'GAME_DEV', 'Game Developer'

    name = models.CharField(max_length=100)
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
        blank=True,
    )
    skills = models.ManyToManyField(
        to='Skill',
        blank=True,
    )


class Skill(models.Model):
    name = models.CharField(max_length=100
                            , unique=True)


