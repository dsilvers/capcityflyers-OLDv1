"""
Random photos context processor.
Returns 6 random photos

Could be slow if there's a LOT of photos, but we aren't going to care here...

Requires 'photos.context_processors.random_gallery' to be set in the context
processors in settings.py
"""

from django.core.paginator import Paginator

from photos.models import Photo


def random_gallery(request):

    gallery = Photo.objects.order_by('?')[:6]

    if gallery.count() == 0:
        return { 'random_gallery': [] }

    p = Paginator(gallery, 1)

    # page_range starts at 1
    # gallery list starts at 0
    # So... the offset needs to be doubled to avoid an off-by-one error
    # It's a bit of a mess?
    for image_number in p.page_range:
        if image_number != 1:
            prev = gallery[image_number - 2].id
        else:
            prev = None
        if image_number != len(gallery):
            next = gallery[image_number].id
        else:
            next = None
        gallery[image_number - 1].prev_id = prev
        gallery[image_number - 1].next_id = next

    return { 'random_gallery': gallery }