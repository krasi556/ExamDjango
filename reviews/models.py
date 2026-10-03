from django.db import models


# Create your models here.


class Review(models.Model):
    employee = models.ForeignKey(
        to='Employee',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveIntegerField()
