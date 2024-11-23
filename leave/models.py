from django.contrib.auth.models import User
from django.db import models


class LeaveApplication(models.Model):
    EMPLOYEE = "employee"
    MANAGER = "manager"

    ROLE_CHOICES = [
        (EMPLOYEE, "Employee"),
        (MANAGER, "Manager"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="leaves"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=LeaveApplication.ROLE_CHOICES,
        default=LeaveApplication.EMPLOYEE,
    )

    def __str__(self):
        return self.user.username
