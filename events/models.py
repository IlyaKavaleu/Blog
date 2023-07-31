from django.db import models


class Event(models.Model):
    """Model Event"""
    event_image = models.ImageField(upload_to='event_images/')
    event_text = models.CharField(max_length=300)

    def __str__(self):
        """Return text style in admin panel"""
        return self.event_text


