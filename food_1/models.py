from django.db import models

# Create your models here.

class First(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title =models.CharField(max_length=100)
    code=models.TextField()
    status=models.BooleanField(default=True)
    language=models.CharField(max_length=100)

    class Meta():
        ordering =['created']