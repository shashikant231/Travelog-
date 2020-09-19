# django uses to constuct database schema and queries
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.title


