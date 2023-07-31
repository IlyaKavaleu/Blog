from django.db import models


class Post(models.Model):
    """Model Post"""
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        """Return text style in admin panel"""
        return self.name
