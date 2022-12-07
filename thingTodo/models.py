from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text 