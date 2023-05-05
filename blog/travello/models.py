from django.db import models

# Create your models here.


class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    img= models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.IntegerField()
    offers = models.BooleanField(default=False)

