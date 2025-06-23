from django.contrib import admin
from .models import Profile

# Register the Profile model so it shows up in the Django Admin.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_manager')
    list_editable = ('is_manager',)
