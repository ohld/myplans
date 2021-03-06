from django.db import models

# Create your models here.
class Plan(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=200, unique=True)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.text