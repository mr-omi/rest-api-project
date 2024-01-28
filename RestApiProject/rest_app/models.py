from django.db import models
import uuid
from django.contrib.auth.models import User


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ToDo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    completed = models.BooleanField()

    def __str__(self):
        return f'{self.title}'
