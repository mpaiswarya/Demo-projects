from django.shortcuts import render
from .models import place,person
# Create your views here.
def web(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj1})