from urllib.parse import urlencode
from django.db.models import Q
from django.views.generic import ListView
from accounts.forms import CustomUserCreationForm, LoginForm
from core.forms import SearchForm, ResumeSearchForm, CategoryForm
from core.models import Resume, Vacancy


class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 20
    model = Vacancy
    context_object_name = 'vacancy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['register_form'] = CustomUserCreationForm()
        context['login_form'] = LoginForm()
        if self.request.user.is_authenticated:
            context['form'] = self.form
            context['categories'] = self.category_form
            if self.search_value:
                context['query'] = urlencode({'search': self.search_value})
        return context

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.category_form = self.get_category_form()
            self.form = self.get_search_form()
            self.search_value = self.get_search_value()
            self.category_value = self.get_category_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.user_role == 'Employer':
                queryset = Resume.objects.filter(is_active=False).order_by('-updated_at')
            else:
                queryset = Vacancy.objects.filter(is_active=False).order_by('-updated_at')
            if self.category_value:
                category = Q(category=self.category_value)
                queryset = queryset.filter(category)
            if self.search_value:
                query = Q(name__icontains=self.search_value)
                queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        if self.request.user.user_role == 'Employer':
            return ResumeSearchForm(self.request.GET)
        return SearchForm(self.request.GET)

    def get_category_form(self):
        return CategoryForm(self.request.GET)

    def get_category_value(self):
        if self.category_form.is_valid():
            return self.category_form.cleaned_data['category']
        return None

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None
