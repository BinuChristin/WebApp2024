from django import forms
from .models import User, Post


class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!= cd['password2']:
            raise forms.ValidationError('Password does not match')
        return cd['password2']

class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','post_title', 'post_description', 'post_shortname', 'post_image')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('post_title', 'post_description', 'post_shortname', 'post_image')
