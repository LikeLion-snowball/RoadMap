from django.shortcuts import render

# Create your views here.
def myPage(request):
    return render(request, "myPage.html")
    
def portfolio(request):
    return render(request, "portfolio.html")