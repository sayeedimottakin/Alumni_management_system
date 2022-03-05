from django.db import models
from django.conf import settings
# Create your models here.
class My_Admin_Panel(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)