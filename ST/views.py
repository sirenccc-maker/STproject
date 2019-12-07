from django.shortcuts import render

from django.http import HttpResponse
from .models import Squirrel

def all_squirrel(request):
    squirrels=Squirrel.objects.all()
    context={
            'squirrel':squirrels,
            }
    return render(request,'ST/all.html',context)
# Create your views here.
