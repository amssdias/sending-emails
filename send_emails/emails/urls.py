from django.urls import path
from emails.views import SendMailFormView

urlpatterns = [
    path('send_email/', SendMailFormView.as_view(), name='send_email'),
]
