from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse("Hello,Lets start new django learning!")
    return render(request,'home.html',{'name':'calculate number app'})


def index(request):
    number1 = int(request.POST['num1'])
    number2 = int(request.POST['num2'])
    addition = number1 + number2
    substraction = number1 - number2
    multiplication = number1 * number2
    division = number1 // number2
    return render(request,'index.html',{'add':addition,'sub':substraction,'mul':multiplication,'div':division})