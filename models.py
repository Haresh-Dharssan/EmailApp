from django.db import models

# Create your models here.

class Emails(models.Model):
    subject=models.CharField(max_length=500)
    message=models.TextField()
    email=models.EmailField()
    createdat=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    editedat=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id