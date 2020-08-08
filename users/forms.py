from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

#custom forms
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields
    email is a required field by default since we specified it in USERNAME_FIELD
    """
    # I can specify additional fields for the form here if i want
    #you can refresh django forms to be sure...
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
         #if you specified a field in REQUIRED_FILED you would have to use it here
     

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('email', 'username')

class  RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')
