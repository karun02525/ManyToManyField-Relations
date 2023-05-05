from django.db import models
from django.db.models.query import QuerySet


class CustomManager(models.Manager):
    def get_roll_range(self,r1,r2) -> QuerySet:
        return super().get_queryset().filter(roll__range=(r1,r2)).order_by('roll')