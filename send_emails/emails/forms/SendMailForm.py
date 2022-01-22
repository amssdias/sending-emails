from smtplib import SMTPAuthenticationError, SMTPSenderRefused
from django import forms
from django.core.mail import send_mail


class SendMailForm(forms.Form):
    user_host_email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Your email",
        "aria-label": "Recipient's username",
        "aria-describedby": "basic-addon2",
    }))
    recipient = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Friend email",
        "aria-label": "Friend email",
    }))
    recipient_server = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Server",
        "aria-label": "Server",
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "id": "exampleInputPassword1",
        "placeholder": "Password",
    }))
    subject = forms.CharField(min_length=1, max_length=120, widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "Subject",
        "placeholder": "Subject",
    }))
    message = forms.CharField(min_length=1, widget=forms.Textarea(attrs={
        "class": "form-control",
        "id": "message",
        "rows": "4",
        "aria-label": "with textarea",
    }))
