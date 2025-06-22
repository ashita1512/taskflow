# In src/tasks/serializers.py

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # This makes the owner field appear as the user's username, not just their ID.
    # It's also read-only, so it can't be set by the API user directly.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        # Add 'owner' to the list of fields
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'owner']