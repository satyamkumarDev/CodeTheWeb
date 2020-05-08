from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=20)
    content = models.TextField()
    slug = models.CharField(max_length=150)
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return  self.title + ' by '+ self.author

class BlogComment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return  self.comment[0:5] + " ... " + " by " + self.user.email



