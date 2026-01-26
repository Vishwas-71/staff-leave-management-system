from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Leave(models.Model):
  user = models.ForeignKey(User , on_delete= models.CASCADE)
  leave_type = models.CharField(max_length=50)
  start_date = models.DateField()
  end_date = models.DateField()
  reason = models.TextField()
  status = models.CharField(max_length=10 , default="pending")


  def __str__(self):
    return self.user.username