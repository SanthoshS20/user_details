from django.db import models

# Create your models here.
class UserDetail(models.Model):
  username = models.CharField(max_length=20, unique="True")
  email_id = models.EmailField(max_length=50, unique="True")
  password = models.CharField(max_length=20)
  confirm_password = models.CharField(max_length=20)
  
  class Meta:
    db_table = "user_detail"