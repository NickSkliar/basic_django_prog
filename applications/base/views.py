from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page(request):
    # return render(request, 'index.html')
    return HttpResponse("hello!")