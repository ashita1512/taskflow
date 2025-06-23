from django.contrib import admin
from .models import LeaveRequest

# Register your models here to make them visible in the admin panel.
@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'start_date', 'end_date', 'status', 'created_at')
    list_filter = ('status', 'owner')
    search_fields = ('owner__username', 'reason')

