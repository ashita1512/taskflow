from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LeaveRequest
from .serializers import LeaveRequestSerializer
from .tasks import send_leave_request_notification
from .permissions import IsManager # <-- Import our new custom permission

class LeaveRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows:
    - Employees to create and view their leave requests.
    - Managers to view all leave requests and approve/reject them.
    """
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        If the user is a manager, return all leave requests.
        Otherwise, return only the requests for the currently authenticated user.
        """
        if self.request.user.profile.is_manager:
            return LeaveRequest.objects.all().order_by('-created_at')
        return self.request.user.leave_requests.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Set the owner of the leave request to the logged-in user.
        """
        instance = serializer.save(owner=self.request.user)
        send_leave_request_notification.delay(instance.id, instance.owner.username)

    @action(detail=True, methods=['post'], permission_classes=[IsManager])
    def approve(self, request, pk=None):
        """
        Custom action for a Manager to approve a leave request.
        """
        leave_request = self.get_object()
        leave_request.status = 'APPROVED'
        leave_request.save()
        # You could trigger another notification task here if you wanted
        return Response({'status': 'leave request approved'})

    @action(detail=True, methods=['post'], permission_classes=[IsManager])
    def reject(self, request, pk=None):
        """
        Custom action for a Manager to reject a leave request.
        """
        leave_request = self.get_object()
        leave_request.status = 'REJECTED'
        leave_request.save()
        return Response({'status': 'leave request rejected'})

