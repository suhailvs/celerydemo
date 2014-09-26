from django.db import models

# Create your models here.
class Code(models.Model):	
    codes=models.CharField(max_length=50)
    sub_result=models.TextField(blank=True)