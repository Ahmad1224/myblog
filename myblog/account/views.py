from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'account/register1.html')