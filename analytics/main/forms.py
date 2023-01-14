from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser, User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", )

