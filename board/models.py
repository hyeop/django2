from django.db import models
from acc.models import User
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pubdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject