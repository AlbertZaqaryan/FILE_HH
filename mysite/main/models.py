from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadFile(models.Model):

    page_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_file')
    file = models.FileField('File')

