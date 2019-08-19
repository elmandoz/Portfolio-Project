from django.db import models
import datetime
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
# Create your models here.
class Blog(models.Model):
    title = models.CharField(blank=True, max_length=100)
    pub_date = models.DateField(default=datetime.datetime.today)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
