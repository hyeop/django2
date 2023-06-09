from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pic = models.ImageField()
    age = models.IntegerField(default=0)
    comment = models.TextField()

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"
    
