from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField('Email почта', max_length=255)
    number_of_telephone = models.CharField('Номер телефона', max_length=255)
    message = models.TextField('Собщение')
    sent_at = models.DateField(auto_now_add=True)



