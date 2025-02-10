from django.db import models

class ExcelAnalysis(models.Model):
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/")
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('configured', 'Configured'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    error_message = models.TextField(null=True, blank=True)
    config = models.JSONField(null=True, blank=True)
    validation_results = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.filename
