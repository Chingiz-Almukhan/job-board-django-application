from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from accounts.forms import CustomUserCreationForm, LoginForm
from accounts.models import Profile
from core.models import Vacancy


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'something'
    model = Profile

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['register_form'] = CustomUserCreationForm()
        context['login_form'] = LoginForm()
        context['vacancies'] = Vacancy.objects.filter(is_active=False).order_by('-updated_at')
        return context

