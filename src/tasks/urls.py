from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeaveRequestViewSet # Import the renamed viewset

router = DefaultRouter()
# The endpoint is now 'leave-requests' and uses the correct viewset and basename
router.register(r'leave-requests', LeaveRequestViewSet, basename='leaverequest')

urlpatterns = [
    path('', include(router.urls)),
]
