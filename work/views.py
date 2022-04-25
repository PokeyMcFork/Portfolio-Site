from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def work(request):
    return render(request, 'work/work.html')