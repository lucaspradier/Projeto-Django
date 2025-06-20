from django.db import models
from django.utils import timezone

#id (primary key)
#first_name (string), last_name (string), phone (string)
#email (email), created_date (date), description (text)
#category (foreign key), show (boolean), owner (foreign key)
#picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)
    #show = models.BooleanField(default=True)
    #owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    