from django.db import models
from django.contrib.auth.models import User
from Fee_App.models import Fee

class StudentRecords(models.Model):
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="registered_students")
    name = models.CharField(max_length=100)
    admission_number = models.IntegerField(unique=True)  # Ensures uniqueness
    grade = models.CharField(max_length=50, default="Unknown")
    guardian_name = models.CharField(max_length=100, default="Unknown") # Added guardian name
    guardian_contact = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.admission_number})"
