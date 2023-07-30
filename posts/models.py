from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name
