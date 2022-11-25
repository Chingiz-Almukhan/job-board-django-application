from urllib.parse import urlencode
from django.db.models import Q
from django.views.generic import ListView
from accounts.forms import CustomUserCreationForm, LoginForm
from core.forms import SearchForm, ResumeSearchForm
from core.models import Resume, Vacancy


class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 1
    model = Vacancy
    context_object_name = 'vacancy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['register_form'] = CustomUserCreationForm()
        context['login_form'] = LoginForm()
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.user_role == 'Employer':
            queryset = Resume.objects.filter(is_active=False).order_by('-updated_at')
        else:
            queryset = Vacancy.objects.filter(is_active=False).order_by('-updated_at')
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        if self.request.user.user_role == 'Employer':
            return ResumeSearchForm(self.request.GET)
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None
