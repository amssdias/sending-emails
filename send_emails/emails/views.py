from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def send(request):
    if request.method == "POST":
        email_host_user = request.POST.get('user_host_email')
        recipient_server = request.POST.get('recipient_server')
        recipient = f"{request.POST.get('recipient')}@{recipient_server}"
        password = request.POST.get('password')
        subject = request.POST.get('subject') or "No Subject"
        message = request.POST.get('message') or "No message"

        try:
            send_mail(
                subject, message, email_host_user, [recipient], 
                auth_user=email_host_user, auth_password=password
            )
        except:
            context = {'message': 'User or password not accepted. Try again.'}
            return render(request, 'emails/index.html', context=context)

        return HttpResponseRedirect("send_email")
    else:
        return render(request, 'emails/index.html')
