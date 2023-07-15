# views.py

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            to_email = form.cleaned_data.get('to_email', '')  # Obtener el campo "to_email" o asignar un valor predeterminado
            
            send_mail(subject, message, from_email, [to_email])
            
            return render(request, 'email_sent.html')
    else:
        form = EmailForm()
    
    return render(request, 'send_email.html', {'form': form})
