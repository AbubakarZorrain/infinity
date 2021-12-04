from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from infinityapp.forms import CreateUserForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from .forms import *
from .models import *
#from .cart import Cart
#from .context_processor import cart_total_amount
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def home(request):
    # user = User.objects.create_user('ali@ali.com', 'johnpassword')
    # user.is_staff = True
    # user.save()
    # #company = get_company(request)
    # # if company is None:
    # #     return HttpResponseRedirect(reverse('customers:login'))
    return render(request, "infinityapp/index.html")

def login(request):
    # user = User.objects.create_user('ali@ali.com', 'johnpassword')
    # user.is_staff = True
    # user.save()
    # #company = get_company(request)
    # # if company is None:
    # #     return HttpResponseRedirect(reverse('customers:login'))
    return render(request, "infinityapp/login.html")

def register(request):
    if request.method == 'POST':

        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('infinityapp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return HttpResponse('Please fill the form correctly')
    else:
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'infinityapp/register.html',context)

    return render(request, "infinityapp/register.html")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

