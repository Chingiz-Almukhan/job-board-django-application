from django import forms

from core.models import Vacancy, Education, Resume, CATEGORY, Job


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'salary', 'description', 'experience', 'category', 'is_active']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск вакансий")


class ResumeSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск резюме по категории")


class ResumeChangeForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY, label='Категория вакансии', required=True)
    telegram = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Введите ссылку на телеграм', 'class': "form-control"}))
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Введите почту', 'class': "form-control"}))
    phone_number = forms.CharField(required=True, label='номер телефона', widget=forms.TextInput(
        attrs={'placeholder': 'Введите номер телефона', 'class': "form-control"}))

    class Meta:
        model = Resume
        fields = ('name', 'category', 'about', 'salary', 'telegram', 'email', 'phone_number', 'linkedin', 'facebook')
        required_fields = ['category', 'telegram', 'email', 'phone_number']


class DateInput(forms.DateInput):
    input_type = 'date'


class EducationAddEditForm(forms.ModelForm):
    study = forms.CharField(required=True, label='Название', widget=forms.TextInput(
        attrs={'placeholder': 'Введите название', 'class': "form-control"}))
    start_date = forms.DateField(widget=DateInput, label='Дата начала обучения', required=True)
    end_date = forms.DateField(widget=DateInput, label='Дата окончания обучения', required=True)

    class Meta:
        model = Education
        fields = ('study', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})


class JobAddEditForm(forms.ModelForm):
    company = forms.CharField(required=True, label='Название', widget=forms.TextInput(
        attrs={'placeholder': 'Введите название', 'class': "form-control"}))
    description = forms.CharField(required=True, label='Обязанности', widget=forms.TextInput(
        attrs={'placeholder': 'Введите свои обязанности', 'class': "form-control"}))
    start_date = forms.DateField(widget=DateInput, label='Дата начала обучения', required=True)
    end_date = forms.DateField(widget=DateInput, label='Дата окончания обучения', required=True)

    class Meta:
        model = Job
        fields = ('description', 'company', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})
