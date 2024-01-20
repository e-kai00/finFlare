from django.db import models
from cloudinary.models import CloudinaryField


class Contact(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    content = models.TextField()
    contact_image = CloudinaryField('image', default='placeholder')
    def __str__(self):
        return self.title
