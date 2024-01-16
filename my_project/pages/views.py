from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'pages\main.html')
def opinion(request):
    return render(request,'pages\opinion.html')
def opinion_1(request):
    return render(request,'pages\opinion_1.html')
def opinion_1_article1(request):
    return render(request,'pages\opinion_1_article1.html')
def opinion_2(request):
    return render(request,'pages\opinion_2.html')
def policits(request):
    return render(request,'pages\politics.html')
def opinion(request):
    return render(request,'pages\opinion.html')
def public(request):
    return render(request,'pages\public.html')
def economy(request):
    return render(request,'pages\economy.html')
def sports(request):
    return render(request,'pages\sports.html')
def entertainment(request):
    return render(request,'pages\entertainment.html')
