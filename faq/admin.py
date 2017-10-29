from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableTabularInline

from faq.models import Section, FAQ

admin.site.register(Section, SortableAdmin)
admin.site.register(FAQ, SortableAdmin)
