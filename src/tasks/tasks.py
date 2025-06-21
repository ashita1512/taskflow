# In src/tasks/tasks.py

from celery import shared_task
import time

@shared_task
def send_creation_notification(task_id, task_title):
    """
    A dummy task that simulates sending an email notification.
    """
    print(f"Starting notification for Task ID: {task_id}...")
    # Simulate a slow network call (e.g., to an email server)
    time.sleep(5) 
    print(f"Successfully sent notification for task: '{task_title}' (ID: {task_id})")
    return f"Notification sent for Task ID: {task_id}"