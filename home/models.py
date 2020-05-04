from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content = models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return ' Messages from '+ self.name + ' -- '+' and his email id is '+ self.email