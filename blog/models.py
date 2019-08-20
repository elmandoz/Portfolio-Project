from django.db import models
import datetime
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=100)
    pub_date = models.DateField(default=datetime.datetime.today)
    body = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")




    def __str__(self):
        return '{} (ID:{})'.format(self.title, self.id)

    def summary(self):
        return self.body[:100]


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
