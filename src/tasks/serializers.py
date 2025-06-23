from rest_framework import serializers
from .models import LeaveRequest

# The serializer is renamed and updated for the new model
class LeaveRequestSerializer(serializers.ModelSerializer):
    # This makes the owner field appear as the user's username for readability
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LeaveRequest
        # List all the fields you want to be visible in the API
        fields = [
            'id', 
            'owner', 
            'start_date', 
            'end_date', 
            'reason', 
            'status', 
            'created_at', 
            'updated_at'
        ]
        # Status should be read-only for employees creating a request
        read_only_fields = ['status', 'owner']

