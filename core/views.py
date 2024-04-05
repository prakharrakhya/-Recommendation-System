from django.shortcuts import render , redirect
from .forms import RegisterForm , LoginForm
#Authenticate
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate 
#check isLogined
from django.contrib.auth.decorators import login_required

# Create your views here.
def core_home(request):
    return render(request , 'core/index.html')

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request=request , data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request=request 
                                , username=username,
                                password=password)
            
            if user is not None:
                auth.login(request , user)
                return redirect('/')
    
    context = {'form':form}
            
    return render(request , 'core/login.html' , context)

def register(request):
    
    #get form
    form = RegisterForm()
    
    if (request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    
    context = {"form":form}
      
    return render(request , 'core/register.html' , context)

@login_required(login_url='/login/')
def dashboard(request):
    print(request.user)
    return render(request , 'core/dashboard.html')

@login_required(login_url='/login/')
def user_logout(request):
    auth.logout(request)
    return redirect('/login/')