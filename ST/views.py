from django.shortcuts import render
from .forms import SquirrelForm
from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import redirect
11
def all_squirrel(request):
    squirrels=Squirrel.objects.all()
    context={
            'squirrels':squirrels,
            }
    return render(request,'ST/all.html',context)

def edit_squirrel(request,squirrel_id):
    squirrel=Squirrel.objects.get(Squirrel_ID=squirrel_id)
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

def show_map(request):
    squirrels=Squirrel.objects.all()
    context={'squirrels':squirrels}
    return render(request, 'ST/show_map.html', context)

def stats(request):
    squirrels=Squirrel.objects.all()
    squirrels_n=squirrels.count()
    context={
            'adult_squirrels':squirrels.filter(Age='Adult').count(),
            'juvenile_squirrels':squirrels.filter(Age='Juvenile').count(),
            'gray_squirrels':squirrels.filter(Primary_Fur_Color='Gray').count(),
            'cinna_squirrels':squirrels.filter(Primary_Fur_Color='Cinnamon').count(),
            'black_squirrels':squirrels.filter(Primary_Fur_Color='Black').count(),
            'Ground_Plane':squirrels.filter(LOCATION='Ground Plane').count(),
            'Above_Ground':squirrels.filter(LOCATION='Above Ground').count(),
            'Running_True':squirrels.filter(Running=True).count(),
            'Running_False':squirrels.filter(Running=False).count(),
            "Tail_flag_True":squirrels.filter(Tail_flags=True).count(),
            "Tail_flag_False":squirrels.filter(Tail_flags=False).count(),
            'Moan_True':squirrels.filter(Moans=True).count(),
            "Moan_False":squirrels.filter(Moans=False).count(),
            }
    return render(request, 'ST/stats.html', context)

