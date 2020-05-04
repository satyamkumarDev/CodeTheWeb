from django.db import models

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