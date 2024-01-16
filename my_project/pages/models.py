
from django.db import models

class article(models.Model):
    CATEGORY_CHOICES = [
        ('opinion_1', 'opinion_1'),
        ('opinion_2', 'opinion_2'),
    ]

    title = models.CharField(max_length=150)
    content = models.TextField()
    date = models.DateTimeField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.title