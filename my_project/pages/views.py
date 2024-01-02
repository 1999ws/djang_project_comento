from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'pages\main.html')
def opinion(request):
    return render(request,'pages\opinion.html')