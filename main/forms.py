from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from .models import *

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@vstlivestockcorporation.net'):
            raise forms.ValidationError("You must use a VST email address.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin_user = True
        if commit:
            user.save()
            self.send_verification_email(user)
        return user

    def send_verification_email(self, user):
        verification_code = get_random_string(length=6, allowed_chars='0123456789')
        user.verification_code = verification_code
        user.verification_code_expiration = timezone.now() + timedelta(hours=1)
        user.save()
        
        send_mail(
            'Your Verification Code',
            f'Your verification code is {verification_code}.',
            'noreply@vstlivestockcorporation.net',
            [user.email],
            fail_silently=False,
        )

class VerificationForm(forms.Form):
    code = forms.CharField(max_length=6, required=True, help_text='Enter the verification code sent to your email.')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'thumbnail']

class EventImageForm(forms.ModelForm):
    class Meta:
        model = EventImage
        fields = ['image']

class UpcomingEventsCarouselForm(forms.ModelForm):
    class Meta:
        model = UpcomingEventsCarouselImage
        fields = ['image', 'caption']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'question_type', 'radio_choices']
        widgets = {
            'radio_choices': forms.TextInput(attrs={'placeholder': 'Choice 1, Choice 2'})
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['radio_choices'].required = False

        if self.instance and self.instance.question_type == 'radio':
            self.fields['radio_choices'].required = True
