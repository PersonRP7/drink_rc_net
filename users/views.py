from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserRegisterCaptchaForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from .models import CustomUser
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
import traceback
from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET


@login_required
def userprofile_redirect(request):
    return HttpResponseRedirect(
        reverse(
            'users:profile',
            kwargs = {"username":request.user.username}
        )
    )

def home(request):
    return render(request, 'users/home.html')


def send_email(user, request, form):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    message = render_to_string('users/activate_account.html', {
        'user':user,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })
    to_email = form.cleaned_data.get('email')
    email = EmailMessage(email_subject, message, to = [to_email])
    email.send()


def register_get(request, messages, redirect, UserRegisterCaptchaForm):
    if CustomUser.objects.filter(
        username = request.user.username
    ).exists():
        messages.info(request, "You already have an account.")
        return redirect('users:profile')
    form = UserRegisterCaptchaForm()
    return render(request, 'users/register.html', {'form':form})


def register_post(request, messages, redirect, UserRegisterCaptchaForm):
    try:
        form = UserRegisterCaptchaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = CustomUser.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            user.is_active = False
            user.save()
            if user:
                send_email(user, request, form)
                # Send message here: "Email sent". Redirect to home
                # return HttpResponse("Email sent.")
                messages.info(request, "Email sent")
                return redirect('users:home')
        else:
            messages.info(request, "Form not correct.")
            return render(
                request,
                'users/register.html',
                {'form':form}
            )
    except Exception as e:
        logging.error(traceback.format_exc())
        return HttpResponse("An error occurred.")
        #Something to show the user here...


def register(request):
    if request.method == 'GET':
        return register_get(request, messages, redirect, UserRegisterCaptchaForm)
    elif request.method == 'POST':
        return register_post(request, messages, redirect, UserRegisterCaptchaForm)


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # redirect to login
        # return HttpResponse('Account activated.')
        messages.info(request, "Account activated. You can now login.")
        return redirect('users:login')
    else:
        return HttpResponse('Link incorrect.')


@login_required
def profile(request, username = None):
    username = request.user.username
    return render(
        request,
        'users/profile.html',
        {'username':username}
    )