from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings


# Send arbitrary Email to users
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient, ])
            return render(request, 'email_sent.html')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})


