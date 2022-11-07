from django.db import models
from django.contrib.auth.models import User
#from autoslug import AutoSlugField
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill

# Create your models here.

def user_directory_path(instance, filename): # Создание папка с контентом под каждого пользователя
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class  ChatUser(User):
    avatar = models.ImageField(upload_to=user_directory_path, height_field = 150, width_field = 150, default='avatars/default.jpg') #height_field=None, width_field=None Имя поля модели, которое будет автоматически 
    #заполняться высотой изображения при каждом сохранении экземпляра модели. ImageField.width_field - Имя поля модели, которое будет автоматически заполняться шириной изображения при каждом сохранении экземпляра модели.
#    avatar_thumbnail = ImageSpecField (source = 'avatar', 
#        processors = [ResizeToFill(150,150)],
#        format = 'JPEG',
#        options = {'quality': 100})

class Room (models.Model):
    creater = models.ForeignKey(ChatUser, verbose_name='Создатель', on_delete=models.CASCADE)
    invited = models.ManyToManyField(ChatUser, verbose_name='Участники', related_name='invited')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чатов'

class Message(models.Model):
    room = models.ForeignKey(Room, verbose_name='Комната чата', on_delete=models.CASCADE)
    user = models.ForeignKey(ChatUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"