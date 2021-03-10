from django import forms 
  
# import GeeksModel from models.py 
from .models import Appeal, Donation
  
# create a ModelForm 
class AppealForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Appeal
        fields = ('title', 'description', 'amount', 'address', 'image')

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief Title of your appeal'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deeply explain' }), 
        'amount': forms.TextInput(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'image': forms.ImageField(),

        }




class DonationForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Donation 
        fields = "__all__"        