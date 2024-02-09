from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .forms import TodoForm
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = UserCreationForm()
    return render(request,"register.html",context={"form":form})

def login_page(request):
    print("hello")
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request,"login.html",context={"form":form})

def logout_page(request):
    logout(request)
    return redirect("/")


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        mainuser=request.user
        form=TodoForm()
        todo=Todo.objects.filter(user=mainuser)
        return render(request,"index.html",context={"form":form,"todos":todo})

def create_todo(request):
    if request.user.is_authenticated:
        mainuser=request.user
        todo=TodoForm(request.POST)

        if todo.is_valid():
            todo=todo.save(commit=False)
            todo.user = mainuser
            todo.save()

        return redirect("/")
    
    return render(request,"index.html")

def delete_todo(request,id):
    # print(request)
    Todo.objects.filter(id=id).delete()
    return redirect('home')

def edit_todo(request,id,status):
    todo = Todo.objects.filter(id=id).update(status=status)
    # todo.status=status
    # todo.save()
    return redirect("/")