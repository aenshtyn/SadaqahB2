from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class Appealer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Tag(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name




class Appeal(models.Model):
    appealer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)
    amount = models.IntegerField (default='1')
    address = models.CharField(max_length = 30, default= '')
    image = models.ImageField(upload_to='appeals/', height_field=None, width_field=None, max_length=100, default ='')
    # due = models.DateTimeField(auto_now=False, auto_now_add=False,default="2020-12-12 00:00")


    def __str__(self):
        return self.title

class Donation(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField()
    amount = models.IntegerField (default='1')
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Admin(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.name