from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    

    def clean(self):
        if not self.content and not self.video:
            raise ValidationError('You must provide either content or a video')

    def __str__(self):
        return self.title
