from django.shortcuts import render

# Create your views here.
def jaga(request):
    return render(request,'jaga.html')

def ramu(request):
    return render(request,'ramu.html')