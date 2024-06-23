
from Accounts.models import CustomUser,Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmailForm
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login

def send_custom_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient],
                fail_silently=False,
            )

            messages.success(request, 'Email sent successfully.')
            return redirect('Email:send_custom_email')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})



def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = CustomUser.objects.get(email=email)
            token = get_random_string(30)  # Generate a random token
            profile, created = Profile.objects.get_or_create(user=user)
            profile.reset_token = token
            profile.save()

            # Build and print the reset link for debugging
            reset_link = request.build_absolute_uri(f'/email/reset_password/{token}/')
            print(reset_link)  # Debugging line

            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, 'password_reset_done.html')
        except CustomUser.DoesNotExist:
            return render(request, 'password_reset_form.html', {'error': 'No user with this email address exists.'})
    return render(request, 'password_reset_form.html')

def password_reset_confirm(request, token):
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        try:
            profile = Profile.objects.get(reset_token=token)
            user = profile.user
            user.set_password(new_password)
            profile.reset_token = ''
            profile.save()
            user.save()
            login(request, user)
            return redirect('Accounts:profile')  # Adjust the redirect as necessary
        except Profile.DoesNotExist:
            return render(request, 'password_reset_confirm.html', {'error': 'Invalid token.'})
    return render(request, 'password_reset_confirm.html', {'token': token})


