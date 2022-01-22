from smtplib import SMTPException, SMTPResponseException, SMTPServerDisconnected

from django.urls import reverse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .forms import SendMailForm

@method_decorator(csrf_exempt, name="dispatch")
class SendMailFormView(FormMixin, TemplateResponseMixin, View):
    form_class = SendMailForm
    success_url = 'emails/send_email/'
    template_name = "emails/form.html"

    def get_success_url(self):
        return reverse("send_email")

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, 'emails/form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user_host_email = form.cleaned_data.get('user_host_email')
        recipient_server = form.cleaned_data.get('recipient_server')
        recipient = f"{form.cleaned_data.get('recipient')}@{recipient_server}"
        password = form.cleaned_data.get('password')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        try:
            send_mail(
                subject, 
                message, 
                user_host_email, 
                [recipient], 
                auth_user=user_host_email, 
                auth_password=password,
            )

        except SMTPException as error:
            context = self.get_context_data(error)
            context["form"] = form

            return render(self.request, self.template_name, context=context, status=400)

        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        if args:
            error = args[0]
            if isinstance(error, SMTPResponseException):
                context["error"] = error.smtp_error.decode("utf-8")
            elif isinstance(error, SMTPServerDisconnected):
                context["error"] = "Server unexpectedly disconnected. Try again."
            elif isinstance(error, Exception):
                context["error"] = "Something went wrong. Try again later."
        return context
