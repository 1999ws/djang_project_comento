from django.db import models

# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title