# In src/tasks/views.py

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_creation_notification

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks.all().order_by('-created_at')

    # THIS IS THE METHOD WITH THE FIX
    def perform_create(self, serializer):
        # This line automatically adds the logged-in user as the owner
        # before the task is saved to the database.
        instance = serializer.save(owner=self.request.user)
        
        # This line sends the notification, which runs after the task is saved.
        send_creation_notification.delay(instance.id, instance.title)