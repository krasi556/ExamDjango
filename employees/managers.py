from django.db import models
from django.db.models import Avg


class EmployeeTopManager(models.Manager):
    def get_avg_rating(self):
        return (
            self
            .annotate(avg_rating=(Avg('reviews__rating')))
        )

    def get_top_rated(self):
        return (self
                .get_avg_rating()
                .filter(avg_rating__isnull=False)
                .order_by('-avg_rating','id')
                .first()
                )