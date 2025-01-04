from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":
         data=request.POST
         receipe_name=data.get('receipe_name')
         receipe_description=data.get('receipe_description')
         receipe_image=request.FILES.get('receipe_image')
         
         Recipe.objects.create(
              receipe_name=receipe_name,
              receipe_description=receipe_description,
              receipe_image=receipe_image,
         )

         return redirect('/receipes/')  # Matches the URL pattern
    queryset=Recipe.objects.all()
    
    context={'receipes':queryset}
    
    return render(request,'receipes.html',context)
 
@login_required(login_url="/login/")
def delete_receipe(request,id):
  queryset=Recipe.objects.get(id=id)
  queryset.delete()
  return redirect('/receipes/')

def update_receipe(request,id):
    queryset=Recipe.objects.get(id=id)

    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            
            queryset.receipe_image = receipe_image
            queryset.save()
        return redirect('/receipes/')

    context={'receipe':queryset}
    return render(request,'update_receipes.html',context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not  User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')

    return render(request,"login.html")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")  # Use error message
            return redirect('/register/')  # Redirect back to the registration page

        # Create the new user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully!")  # Success message
         # Redirect to the login page after successful registration

    return render(request, "register.html")

def log_out(request):
    logout(request)
    return redirect('/login/')