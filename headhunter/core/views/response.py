from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from django.views.generic import CreateView, ListView, DetailView

from core.models import ResponseChat, Message


class ResumeAddResponseView(CreateView):
    model = ResponseChat

    def post(self, request, *args, **kwargs):
        for response in ResponseChat.objects.all():
            if response.resume.pk == int(request.POST['resume']) and response.vacancy.pk == int(
                    request.POST['vacancy']):
                return HttpResponseBadRequest('error')
        resp = ResponseChat.objects.create(vacancy_id=request.POST['vacancy'], resume_id=request.POST['resume'])
        Message.objects.create(chat=resp, user=request.user, text=request.POST['message'])
        return HttpResponse('success')


class AddMessageToResponse(View):
    def post(self, request, *args, **kwargs):
        response = get_object_or_404(ResponseChat, pk=kwargs['pk'])
        Message.objects.create(chat=response, user=request.user, text=request.POST['message'])
        return redirect('show_responses')


class ShowResponse(ListView):
    model = ResponseChat
    template_name = 'user_response.html'
    context_object_name = 'responses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
