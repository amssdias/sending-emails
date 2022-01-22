from django.urls import reverse, resolve
from django.test import TestCase, Client

from emails.forms import SendMailForm
from emails.views import SendMailFormView


class TestEmails(TestCase):

    def setUp(self):
        self.client = Client()
        self.send_email_url = reverse("send_email")
        self.send_mail_data = {
            "user_host_email": "testing@hotmail.com",
            "recipient": "recipient_test",
            "recipient_server": "@hotmail.com",
            "password": "1234567",
            "subject": "This is subject of email",
            "message": "This is the message",
        }

        self.send_email_missing_data = {
            "user_host_email": "testing@hotmail.com",
            "recipient": "",
            "recipient_server": "@hotmail.com",
            "password": "",
            "subject": "This is subject of email",
            "message": "This is the message",
        }
        return super().setUp()
    
    def test_email_url_resolves(self):
        url = reverse("send_email")
        self.assertEqual(resolve(url).func.view_class, SendMailFormView)

    def test_email_GET(self):
        response = self.client.get(self.send_email_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "emails/form.html")

    def test_email_POST(self):
        with self.settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"):
            response_ok = self.client.post(self.send_email_url, self.send_mail_data)
            self.assertEqual(response_ok.status_code, 302)
            response_bad = self.client.post(self.send_email_url, self.send_email_missing_data)
            self.assertEqual(response_bad.status_code, 400)

    def test_send_email_form_valid(self):
        form_data = {
            "user_host_email": "testing123",
            "recipient": "testing_123",
            "recipient_server": "hotmail.com",
            "password": "12345678",
            "subject": "hi",
            "message": "Hey there",
        }
        send_email_form = SendMailForm(data=form_data)
        self.assertTrue(send_email_form.is_valid())
    
    def test_send_email_form_invalid(self):
        form_data = {
            "user_host_email": "testing123",
            "recipient": "testing_123",
            "recipient_server": "",
            "password": "12345678",
            "subject": "hi",
            "message": "Hey there",
        }
        send_email_form = SendMailForm(data=form_data)
        self.assertFalse(send_email_form.is_valid())
        self.assertEquals(len(send_email_form.errors), 1)