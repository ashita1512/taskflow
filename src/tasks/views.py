# In src/tasks/views.py
# THIS IS A TEST TO SEE IF DOCKER IS SYNCING FILES
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_creation_notification

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """
        Overrides the default create behavior to also trigger our Celery task.
        """
        instance = serializer.save()
        send_creation_notification.delay(instance.id, instance.title)