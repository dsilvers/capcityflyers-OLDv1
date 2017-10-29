from django.db import models
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin


class Section(SortableMixin):
    name = models.CharField(max_length=150)
    section_order = models.PositiveIntegerField(default=0, 
        editable=False, db_index=True)

    class Meta:
        ordering = ['section_order']

    def __str__(self):
        return self.name


class FAQ(SortableMixin):
    question = models.TextField()
    answer = models.TextField()
    section = SortableForeignKey("faq.Section", related_name="faqs")

    faq_order = models.PositiveIntegerField(default=0, 
        editable=False, db_index=True)

    class Meta:
        ordering = ['faq_order']

    def __str__(self):
        return self.question