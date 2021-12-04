from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import EmailField
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    email = EmailField(max_length=200, help_text='Required')
    class Meta:
       model = User
       fields =['username', 'email', 'password1','password2']

