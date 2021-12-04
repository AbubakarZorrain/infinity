from django.shortcuts import render

# Create your views here.
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
    # user = User.objects.create_user('ali@ali.com', 'johnpassword')
    # user.is_staff = True
    # user.save()
    # #company = get_company(request)
    # # if company is None:
    # #     return HttpResponseRedirect(reverse('customers:login'))
    return render(request, "infinityapp/register.html")