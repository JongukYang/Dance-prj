from django.shortcuts import render

# Create your views here.
def classapp(request) :
    return render(request, 'class.html')