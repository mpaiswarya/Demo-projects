from django.shortcuts import render, redirect

from .form import homeforms
from .models import home

# Create your views here.
def data(request):
    data =home.objects.all()
    context = {
        'data_list': data
    }
    return render(request, 'data.html', context)

def detail(request,data_id):
     detail=home.objects.get(id=data_id)
     return render(request,'detail.html',{'detail':detail})

def add_trivago(request):
    if request.method=='POST':
        name=request.POST.get('name')
        place = request.POST.get('place')
        price = request.POST.get('price')
        img=request.FILES['img']
        hotel=home(name=name,place=place,price=price,img=img)
        hotel.save();
    return render(request,'add.html')
def update(request,id):
    hom=home.objects.get(id=id)
    form=homeforms(request.POST or None, request.FILES,instance=hom)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'home':hom})

def delete(request,id):
    if request.method == "POST":
       hom=home.objects.get(id=id)
       hom.delete()
       return redirect('/')

    return render(request,"delete.html")
