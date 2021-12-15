from django.shortcuts import render
from . import views
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from.models import Todo

# Create your views here.

def home(request):
    return render(request,'signup.html')


def index(request):
     all_todo=Todo.objects.all()
     return render(request,'index.html',{"Todo":all_todo})



def addtodo(request):
     if request.method=="POST":
          todo_title=request.POST['todo_title']
          todo_description=request.POST['todo_description']
          Todo.objects.create(title=todo_title,description=todo_description)
          return redirect('/')

     else:
          return redirect('/')
     


def deletetodo(request , id):
     Todo.objects.get(id=id).delete()
     return redirect('/')



def marktodo(request,id):
     todo=Todo.objects.get(id=id)
     todo.completed=True
     todo.save()
     return redirect('/')
     

def unmarktodo(request,id):
     todo=Todo.objects.get(id=id)
     todo.complted=False
     todo.save()
     return redirect('/')



def login(request):
     if request.method=="POST":
          username2=request.POST['username_2']
          password2=request.POST['password_2']

          user = auth.authenticate(username=username2,password=password2)
        
          
          if user is not None:
               
               auth.login(request,user)
               msg="user loged"
               return redirect('/index',{"msg":msg})
          else:
               msg="wrong password"
               return redirect('/login')
            
         
     else:
          print("home")
          return render(request,'login.html')


def signup(request):
     
     if request.method=="POST":
          username1=request.POST['username3']
          password1=request.POST['password3']
          # if len(User.objects.filter(username=username1)) !=0:
               

          new_user = User.objects.create_user(username=username1,password=password1)
          
          
          

          print("Account Created")
          return redirect('/login')
        

     else:
          return render(request,'signup.html')
     

         
def logout(request):
     auth.logout(request)
     return redirect('/')
     