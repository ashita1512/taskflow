from django.db import models
from django.contrib.auth.models import User

# This model extends the built-in User model.
class Profile(models.Model):
    # This creates a one-to-one link. Each User will have exactly one Profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # This boolean field will be our "role". True for managers, False for regular employees.
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        role = "Manager" if self.is_manager else "Employee"
        return f"{self.user.username}'s Profile ({role})"

