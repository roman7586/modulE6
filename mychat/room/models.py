from tkinter import _ImageSpec
from django.db import models
from requests import options

# Create your models here.

def user_directory_path(instance, filename): # Создание папка с контентом под каждого пользователя
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class ChatUser (User):
    avatar = models.ImageField(upload_to=user_directory_path)
    avatar_thumbnail = ImageSpecField (source = 'avatar', 
        processors = [ResizeToFill(150,150)],
        format = 'JPEG',
        options = {'quality': 100})

class Room (models.Model):
    creater = models.ForeignKey(ChatUser, verbose_name='Создатель', on_delete=models.CASCADE)
    