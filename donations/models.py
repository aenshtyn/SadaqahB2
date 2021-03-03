from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

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

    def save_tag(self):
        self.save

class Location(models.Model):
    name = models.CharField(max_length =30)

    @classmethod
    def all_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()




class Appeal(models.Model):
    # appealer = models.ForeignKey(Appealer, on_delete=models.CASCADE, default='admin')
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    published = models.BooleanField(default=False)
    amount = models.IntegerField (default='1')
    address = models.CharField(max_length = 30, default= '')
    image = models.ImageField(upload_to='appeals/', default='appeals/appeal.png')
    # due = models.DateTimeField(auto_now=False, auto_now_add=False,default="2020-12-12 00:00")


    def __str__(self):
        return self.title

    @classmethod
    def all_appeals(cls):
        appeals = Appeal.objects.all()
        return appeals

    @classmethod
    def appeals_by_location(cls,category):
        appeal_location = Appeal.objects.filter(Location)

    def save_appeal(self):
        self.save()

    def delete_appeal(self):
        self.delete()

    class Meta:
        ordering = ['title']

    
class Donation(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField()
    amount = models.IntegerField (default='1')
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_donation(self):
        return self.save()

    def delete_donation(self):
        return self.delete()

    class Meta:
        ordering = ['title']



# class Admin(models.Model):
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name