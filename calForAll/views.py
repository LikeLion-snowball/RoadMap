from django.shortcuts import render

# Create your views here.
def calForAll(request):
    return render(request, 'calForAll.html')