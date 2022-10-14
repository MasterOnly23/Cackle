
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ImageField

from SocialMedia.models import Post, Profile, Country

COUNTRY_CHOICES = (
    ('', '-----'),
    ('Argentina', 'Argentina'),
    ('Belice', 'Belice'),
    ('Bolivia', 'Bolivia'),
    ('Brasil', 'Brasil'),
    ('Canada', 'Canada'),
    ('Chile', 'Chile'),
    ('Colombia', 'Colombia'),
    ('Costa Rica', 'Costa Rica'),
    ('Cuba', 'Cuba'),
    ('Curazao', 'Curazao'),
    ('Aruba', 'Aruba'),
    ('Ecuador', 'Ecuador' ),
    ('El Salvador', 'El Salvador'),
    ('Guatemala', 'Guatemala'),
    ('Haiti', 'Haiti'),
    ('Honduras', 'Honduras'),
    ('Jamaica', 'Jamaica'),
    ('Mexico', 'Mexico'),
    ('Nicaragua', 'Nicaragua'),
    ('Panama', 'Panama'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Puerto Rico', 'Puerto Rico'),
    ('Republica Dominicana', 'Republica Dominicana'),
    ('United States', 'United States'),
    ('Uruguay', 'Uruguay'),
    ('Venezuela', 'Venezuela'),
)



class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=15)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput, max_length=15)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'country']
        help_texts = {k:"" for k in fields}


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Que estas pensando?'}),required=True)

    class Meta:
        model = Post
        fields = ['content'] #asociamos el form a el modelo



class UserEditForm(UserChangeForm):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=15)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password', 'country']
        help_texts = {k:"" for k in fields}

class UserEditCountry(forms.ModelForm):
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)

    class Meta:
        model = Country
        fields = ['country']

class AvatarForm(forms.Form):
    avatar = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['avatar']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget= forms.PasswordInput())
    new_password1 = forms.CharField(label="New Password",widget= forms.PasswordInput())
    new_password2 = forms.CharField(label="Repeat New Password",widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}
