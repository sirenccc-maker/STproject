from django.shortcuts import render

from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import redirect

def all_squirrel(request):
    squirrels=Squirrel.objects.all()
    context={
            'squirrel':squirrels,
            }
    return render(request,'ST/all.html',context)

def edit_squirrel(request,squirrel_id):
    squirrel=Squirrel.object.get(Squirrel_ID=squirrel_id)
    if request.method == 'POST':
        form=SquirrelForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/ST/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
    context={
            'form':form,
            }
    return render(request,'ST/edit.html',context)

def add_squirrel(request):
    if request.method == 'POST':
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/ST/sightings')

    else:
        form = SquirrelForm()

    context={
            'form':form,
            }
    return render(request,'ST/add.html',context)
# Create your views here.
