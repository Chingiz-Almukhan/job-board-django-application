from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core.models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'salary', 'description', 'experience', 'category', 'is_active']
