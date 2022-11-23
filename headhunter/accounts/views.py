from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm
from accounts.models import Profile
from core.models import Vacancy, Resume


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


class EmployerDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "employer_profile.html"
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['resumes'] = Resume.objects.filter(author=user).order_by('-updated_at')
        context['vacancy'] = Vacancy.objects.filter(author=user).order_by('-updated_at')
        context['change_form'] = UserChangeForm(instance=self.object)
        return context


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'employer_profile.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('employer_profile', kwargs={'pk': self.object.pk})
