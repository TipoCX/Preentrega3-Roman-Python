from django.db import models
from django.utils import timezone


# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def sendmessage(self, content, group):
        message = Message.objects.create(content=content, group=group, author=self)


class Group(models.Model):
    alias = models.CharField(max_length=40)
    description = models.CharField(max_length=450)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    def send_create_message(self):
        message = Message.objects.create(content=f"{self.creator} a creado el grupo {self.alias}", group=self, author=self.creator)

class Message(models.Model):
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now)
