from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin_user = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    verification_code_expiration = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='event_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.event.title}"
    
class UpcomingEventsCarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carousel Image {self.id}"

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('radio', 'Radio Button'),
        ('rating_1_5', 'Rating 1-5'),
        ('rating_1_10', 'Rating 1-10'),
    ]
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES, default='text')
    radio_choices = models.CharField(max_length=200, blank=True, help_text='Comma-separated choices for radio buttons')

    def __str__(self):
        return self.text

class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responses', on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

