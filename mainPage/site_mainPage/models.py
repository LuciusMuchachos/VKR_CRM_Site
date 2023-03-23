import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class order_Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text="Unique ID for this particular book across whole library")
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.TextField
    url = models.TextField()
    worker = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_status = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=order_status, blank=True, default='m', help_text='Book availability')

    def __str__(self):
        return self.title