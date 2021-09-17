from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import UserManager

def randomString():
    um = UserManager()
    return( um.make_random_password( length=25 ) )

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, default=randomString, blank=True, null=True)


    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(verbose_name='Capa do Post', blank=True, null=True)
    authorimage = models.ImageField (verbose_name='Foto do Autor', blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, blank=False, null=True)
    slug = models.SlugField(max_length=100, unique=True, default=randomString, blank=True, null=True)
    

    def __str__(self):
        return self.title + '/' + str(self.author)










        