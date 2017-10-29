from django.db import models

from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Aircraft(SortableMixin):
    tailnum = models.CharField("Tail Number", max_length=12, unique=True)
    year = models.IntegerField("Aircraft Year")
    make = models.CharField("Aircraft Make", max_length=40)
    model = models.CharField("Aircraft Model", max_length=40)
    designation = models.CharField("Aircraft Type Designation", max_length=12)

    rate_wet = models.IntegerField("Wet Rate", blank=True)
    rate_dry = models.IntegerField("Dry Rate", blank=True)

    speed = models.IntegerField("Speed in Knots", blank=True)
    useful_load = models.IntegerField("Useful Load", blank=True)

    description = models.TextField("Description", blank=True)

    image = models.ImageField("Primary Image")

    image_large = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 200)],
                                format='JPEG',
                                options={'quality': 72})

    image_small = ImageSpecField(source='image',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 72})

    aircraft_order = models.PositiveIntegerField(default=0, 
        editable=False, db_index=True)

    class Meta:
        ordering = ['aircraft_order']
        verbose_name_plural = "Aircraft"

    def __str__(self):
        return "{} - {} {} {}".format(self.tailnum, self.year, self.make, 
            self.model)

    def featured_equipment(self):
        return self.equipment.objects.filter(aircraft=self, featured=True)

    def image_thumb(self):
        return '<img src="/media/%s" height="100" />' % (self.image)
    image_thumb.allow_tags = True


class AircraftEquipmentCategory(SortableMixin):
    name = models.CharField(max_length=100)

    category_order = models.PositiveIntegerField(default=0, 
        editable=False, db_index=True)

    class Meta:
        ordering = ['category_order']
        verbose_name_plural = "Equipment Categories"

    def __str__(self):
        return self.name


class AircraftEquipment(SortableMixin):
    aircraft = SortableForeignKey("aircraft.Aircraft", related_name="equipment")
    name = models.CharField(max_length=100)
    featured = models.BooleanField("Featured on Frontpage")
    category = models.ForeignKey("aircraft.AircraftEquipmentCategory", 
        related_name="category")

    equipment_order = models.PositiveIntegerField(default=0, 
        editable=False, db_index=True)

    class Meta:
        ordering = ['equipment_order']

    def __str__(self):
        return "{} - {} - {}".format(self.aircraft.tailnum, self.category.name, 
            self.name)


class AircraftGalleryImage(SortableMixin):
    aircraft = SortableForeignKey("aircraft.Aircraft", related_name="gallery")
    image = models.ImageField("Gallery Image")
    description = models.TextField("Image Description")

    image_large = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 200)],
                                format='JPEG',
                                options={'quality': 72})

    image_small = ImageSpecField(source='image',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 72})

    image_order = models.PositiveIntegerField(default=0, 
        editable=False, db_index=True)

    class Meta:
        ordering = ['image_order']

    def __str__(self):
        return "{} - {}".format(self.aircraft.tailnum, self.description)

    def image_thumb(self):
        return '<img src="/media/%s" height="100" />' % (self.image)
    image_thumb.allow_tags = True