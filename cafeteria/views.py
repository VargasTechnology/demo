from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/home.html')


def menu(request):
    return render(request, 'menu/menu.html')