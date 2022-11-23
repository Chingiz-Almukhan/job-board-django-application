from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView

from core.forms import ResumeChangeForm, EducationAddEditForm, JobAddEditForm
from core.models import Resume, Education, Job


class ResumeAddView(CreateView):
    model = Resume

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('edit_resume', pk=resume.pk)


class ResumeEditView(UpdateView):
    model = Resume
    form_class = ResumeChangeForm
    template_name = 'resume_change.html'
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super(ResumeEditView, self).get_context_data(**kwargs)
        context['education_form'] = EducationAddEditForm()
        context['job_form'] = JobAddEditForm()
        return context

    def get_success_url(self):
        return reverse('employer_profile', kwargs={'pk': self.object.author_id})


class AddEducation(View):
    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(pk=kwargs.get('pk'))
        form = EducationAddEditForm(request.POST)
        if form.is_valid():
            study = form.cleaned_data.get('study')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            education = Education.objects.create(study=study, resume=resume, start_date=start_date, end_date=end_date)
            education.save()
        return redirect('edit_resume', pk=kwargs.get('pk'))


class AddJob(View):
    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(pk=kwargs.get('pk'))
        form = JobAddEditForm(request.POST)
        print(form)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            company = form.cleaned_data.get('company')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            job = Job.objects.create(description=description, company=company,
                                     resume=resume, start_date=start_date, end_date=end_date)
            job.save()
        return redirect('edit_resume', pk=resume.pk)


def delete_resume(request, *args, **kwargs):
    resume = Resume.objects.filter(pk=kwargs.get('pk'))
    resume.delete()
    return redirect('employer_profile', pk=request.user.pk)


class ResumeDetailView(DetailView):
    model = Resume
    template_name = "resume_detail.html"
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = Education.objects.filter(resume_id=self.object.pk)
        context['job'] = Job.objects.filter(resume_id=self.object.pk)
        return context


def update_resume(request, *args, **kwargs):
    resume = get_object_or_404(Resume, pk=kwargs['pk'])
    resume.updated_at = timezone.now()
    resume.save()
    return redirect('employer_profile', pk=resume.author_id)
