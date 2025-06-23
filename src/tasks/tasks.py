from celery import shared_task
import time

# The Celery task is renamed for clarity
@shared_task
def send_leave_request_notification(request_id, username):
    """
    A dummy task that simulates sending a notification to a manager
    about a new leave request.
    """
    print(f"Starting manager notification for Leave Request ID: {request_id}...")
    # Simulate a slow network call (e.g., to an email or Slack API)
    time.sleep(5) 
    print(f"Successfully sent new leave request notification for user: '{username}' (Request ID: {request_id})")
    return f"Notification sent for Request ID: {request_id}"
