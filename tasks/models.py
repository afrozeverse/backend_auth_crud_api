from django.db import models
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()

class Task(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    title=models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

