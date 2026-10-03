from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.


class Review(models.Model):
    employee = models.ForeignKey(
        to='employees.Employee',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
