from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm
from accounts.models import Profile
from core.models import Resume, Vacancy


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('main')
        password = form.cleaned_data.get('password')
        if '@' not in form.cleaned_data.get('email'):
            phone = form.cleaned_data.get('email')
            email = Profile.objects.filter(phone_number=phone).values('email')
            if len(email) == 0:
                return redirect('main')
            email_str = email[0]
            user = authenticate(request, email=email_str.get('email'), password=password)
            if not user:
                return redirect('main')
            login(request, user)
            return redirect('main')
        email = form.cleaned_data.get('email')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('main')
        login(request, user)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(TemplateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        return redirect('main')