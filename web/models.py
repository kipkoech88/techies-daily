from django.db import models 
from django.contrib.auth.models import User 
from datetime import datetime

# Create your models here.
class posts(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    image=models.ImageField(null=True, blank=True,)
    title=models.CharField(max_length=200,)  
    date_posted=models.DateTimeField(auto_now=datetime.now())
    post_id=models.IntegerField(null=True, blank=True,) 
    headline=models.TextField(max_length=200, null=False, default="This is the headline") 
    full_story=models.TextField(max_length=1500, null=False, blank=False, default=headline)
    def __str__(self):
        return self.title 

    