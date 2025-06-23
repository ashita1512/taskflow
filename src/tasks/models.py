from django.db import models
from django.contrib.auth.models import User

# The model is renamed from Task to LeaveRequest
class LeaveRequest(models.Model):
    # Choices for the status field
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    # The owner of the request, linked to Django's User model
    owner = models.ForeignKey(User, related_name='leave_requests', on_delete=models.CASCADE)

    # New fields specific to a leave request
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Leave request for {self.owner.username} from {self.start_date}"
