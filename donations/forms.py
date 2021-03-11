from django import forms 
  
# import GeeksModel from models.py 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appeal, Donation, Appealer
  
# create a ModelForm 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # phone_number = forms.CharField(max_length=13, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
class AppealForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Appeal
        fields = "__all__"

class AppealerFrom(forms.ModelForm):

    class Meta:
        model = Appealer
        fields = "__all__"


class DonationForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Donation 
        fields = "__all__"        