from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    professor_image = models.ImageField(upload_to='professor_images/')
    location_image = models.ImageField(upload_to='location_images/')

    def __str__(self):
        return self.title
