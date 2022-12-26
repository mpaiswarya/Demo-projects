from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.form import Taskforms
from todoapp.models import Task
from django.views.generic import  ListView
from django.views.generic import  DetailView
from django.views.generic import  UpdateView,DeleteView

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = "task1"


class DetailListView(DetailView):
    model = Task
    template_name = 'detaillist.html'
    context_object_name = "task"

class UpdateListView(UpdateView):
    model = Task
    template_name = 'updatelist.html'
    context_object_name = "task"
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class DeleteListView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your views here.
def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'task1': task1})


def delete(request,id):
    if request.method == "POST":
       task=Task.objects.get(id=id)
       task.delete()
       return redirect('/')

    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    form=Taskforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})