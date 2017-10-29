from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class Photo(models.Model):
    description = models.TextField(blank=True)
    image = models.ImageField("Gallery Image")

    image_gallery = ImageSpecField(source='image',
                                processors=[ResizeToFit(width=1200)],
                                format='JPEG',
                                options={'quality': 80})

    image_large = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 200)],
                                format='JPEG',
                                options={'quality': 72})

    image_small = ImageSpecField(source='image',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 72})

    def __str__(self):
        if self.description:
            return self.description
        return "No Description"

