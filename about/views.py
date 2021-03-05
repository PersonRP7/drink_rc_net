from django.shortcuts import render
# from products.models import 

def about(request):
    return render(
        request,
        'about/about.html'
    )

def introduction(request):
    return render(
        request,
        'about/introduction.html'
    )

def home(request):
    return render(
        request,
        'about/home.html'
    )

def home2(request):
    return render(
        request,
        'about/home2.html'
    )

def service(request):
    return render(
        request,
        'about/service.html'
    )


