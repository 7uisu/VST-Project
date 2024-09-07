from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserRegistrationForm
    model = CustomUser
    list_display = ('email', 'is_admin_user', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_admin_user', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin_user', 'is_staff', 'is_active')}),
        ('Verification', {'fields': ('verification_code', 'verification_code_expiration')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin_user', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    form = EventForm

admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)
admin.site.register(UpcomingEventsCarouselImage)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')

