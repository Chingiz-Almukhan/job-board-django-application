import datetime

from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.views import View
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from accounts.models import Profile
from core.forms import ResumeChangeForm, EducationAddEditForm, JobAddEditForm
from core.models import Resume, Education, Job, Vacancy


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
        context['education'] = Education.objects.filter(resume_id=self.object.pk)
        context['job'] = Job.objects.filter(resume_id=self.object.pk)
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
        context['vacancy'] = Vacancy.objects.filter(author=self.request.user)
        return context


def update_resume(request, *args, **kwargs):
    resume = get_object_or_404(Resume, pk=kwargs['pk'])
    resume.updated_at = timezone.now()
    resume.save()
    return redirect('employer_profile', pk=resume.author_id)


def download_pdf(request, *args, **kwargs):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Resume' + \
                                      str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    education = Education.objects.filter(resume_id=kwargs.get('pk'))
    job = Job.objects.filter(resume_id=kwargs.get('pk'))
    resume = Resume.objects.filter(pk=kwargs.get('pk'))
    to_str = resume.values('author')[0]
    check = to_str.get('author')
    author = Profile.objects.filter(pk=check)
    html_string = render_to_string('pdf_output.html',
                                   {'author': author, 'resume': resume, 'education': education, 'job': job})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


def hide_resume(request, *args, **kwargs):
    resume = get_object_or_404(Resume, pk=kwargs['pk'])
    if resume.is_active is not True:
        resume.is_active = True
    else:
        resume.is_active = False
    resume.save()
    return redirect('employer_profile', pk=resume.author_id)


class DeleteEducationView(DeleteView):
    model = Education

    def get_success_url(self):
        return reverse('edit_resume', kwargs={'pk': self.object.resume.pk})


class EditEducationView(UpdateView):
    model = Education
    form_class = EducationAddEditForm
    template_name = 'edit_education.html'
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('edit_resume', kwargs={'pk': self.object.resume.pk})


class DeleteJobView(DeleteView):
    model = Job

    def get_success_url(self):
        return reverse('edit_resume', kwargs={'pk': self.object.resume.pk})


class EditJobView(UpdateView):
    model = Job
    form_class = JobAddEditForm
    template_name = 'edit_job.html'
    context_object_name = 'job'

    def get_success_url(self):
        return reverse('edit_resume', kwargs={'pk': self.object.resume.pk})
