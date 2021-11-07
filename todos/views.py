from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import TodosForm
from .models import Todos
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def items(request):
	user=request.user
	todos=Todos.objects.filter(author=user)
	return render(request,"partials/items.html",{"todos":todos})

def create_todo(request):
	form=TodosForm()
	return render(request,"partials/create_todo.html",{"form":form})

def home(request):
	user=request.user
	todos=Todos.objects.filter(author=user)
	form=TodosForm(request.POST or None)

	if request.method=="POST":
		if form.is_valid():
			todo=form.save(commit=False)
			todo.author=user
			todo.save()

			return HttpResponse("")
		else:
			return render(request,"partials/items.html",{"todos":todos})

	return render(request,"home.html",{"form":form,"todos":todos})
	
def details(request,pk):
	todo=Todos.objects.get(id=pk)
	return render(request,"partials/details.html",{"todo":todo})

def delete(request, pk):
    todo= get_object_or_404(Todos, id=pk)

    if request.method == "POST":
        todo.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def update(request, pk):
    todo= Todos.objects.get(id=pk)
    form = TodosForm(request.POST or None, instance=todo)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("details", pk=todo.id)

    context = {
        "form": form,
        "todo": todo
    }

    return render(request, "partials/create_todo.html", context)
