from django.db import models

# Create your models here.

class Novel(models.Model):
    title=models.CharField(max_length=50)
    work_name=models.CharField(max_length=50)
    tag=models.TextField()
    linked=models.TextField()
    summry=models.TextField()
    word_num=models.TextField(null=True)
    
    
    def __str__(self):
        return self.title