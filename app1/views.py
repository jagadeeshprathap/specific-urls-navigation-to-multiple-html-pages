from django.shortcuts import render

# Create your views here.
def ganga(request):
    return render(request,'ganga.html')

def venkat(request):
    return render(request,'venkat.html')