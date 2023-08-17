from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.title
    