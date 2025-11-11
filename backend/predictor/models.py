from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    disease = models.CharField(max_length=255)
    symptoms = models.TextField()  # You can store JSON string or comma-separated symptoms
    medicines = models.TextField()  # Same format as symptoms
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.disease} on {self.date.strftime('%Y-%m-%d')}"
