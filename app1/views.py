from django.shortcuts import render

# Create your views here.
def ziro_valley(request):
    return render(request,'ziro_valley.html')

def child(request):
    return render(request,'child.html')


