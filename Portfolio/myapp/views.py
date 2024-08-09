from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'index.html')

def apple(request):
    return render(request, 'apple2024.html')