from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from accounts.models import ROLE


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Имя', min_length=5, max_length=50, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    email = forms.CharField(label='Email', min_length=7, max_length=70, required=True,
                            widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    avatar = forms.ImageField(label='Аватар', required=False)
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    user_role = forms.ChoiceField(label='Роль', choices=ROLE, required=True,
                                  widget=forms.RadioSelect(attrs={'class': "choose_role_block"}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'avatar', 'password', 'password_confirm', 'phone_number', 'user_role')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


