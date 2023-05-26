# https://docs.djangoproject.com/en/4.2/topics/forms/#more-on-fields


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','first_name','last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','first_name','last_name')
