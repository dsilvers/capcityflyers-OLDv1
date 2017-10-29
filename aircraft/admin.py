from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableTabularInline

from aircraft.models import Aircraft, AircraftEquipment, AircraftGalleryImage, \
    AircraftEquipmentCategory


class InlineImage(SortableTabularInline):
    model = AircraftGalleryImage
    readonly_fields = ('image_thumb',)


class InlineEquipment(SortableTabularInline):
    model = AircraftEquipment


class AircraftAdmin(SortableAdmin):
    inlines = [InlineImage, InlineEquipment]
    readonly_fields = ('image_thumb',)
admin.site.register(Aircraft, AircraftAdmin)


class AircraftEquipmentCategoryAdmin(SortableAdmin):
    model = AircraftEquipmentCategory
admin.site.register(AircraftEquipmentCategory, AircraftEquipmentCategoryAdmin)
