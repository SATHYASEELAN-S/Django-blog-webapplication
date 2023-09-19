from django.db import models
from django.contrib.auth.models import User

class blogpost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    img=models.ImageField(upload_to='uploads/')
    created=models.DateTimeField(auto_now_add=True)
    upated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]
    def __str__(self):
        return self.content[0:484]

class userdetail(models.Model):
    aboutuser=models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    about=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.about
    
 
class Message(models.Model):
    messageuser=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(blogpost,on_delete=models.CASCADE)
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    upated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comments