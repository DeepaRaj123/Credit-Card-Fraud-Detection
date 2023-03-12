from django.shortcuts import render


def base(request):
    return render(request, 'homeApp/landing_page.html')
    

def login2(request):
    return render(request, 'homeApp/login.html')


