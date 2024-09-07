from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from .models import Event, EventImage, UpcomingEventsCarouselImage

@receiver(post_delete, sender=Event)
def delete_event_thumbnail(sender, instance, **kwargs):
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)

@receiver(post_delete, sender=EventImage)
def delete_event_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=UpcomingEventsCarouselImage)
def delete_carousel_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
