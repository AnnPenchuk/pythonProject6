from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    ...
    upload = models.FileField(upload_to=user_directory_path)

class Book(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to = user_directory_path)
    book = models.FileField(upload_to ='books/%Y-%m-%d/')

    def __str__(self):
        return self.title
