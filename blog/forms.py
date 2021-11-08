from django import forms
from .models import Blogs , Users

class AddUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('name' , 'surname' , 'nickname' , 'email' , 'image')