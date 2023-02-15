from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def index(request):
    return render(request, 'api/index.html', {})