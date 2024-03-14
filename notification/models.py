from django.db import models


class EmailMessage(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField()
