from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm




def login_view(request):
    
    if request.method == 'POST':
      
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            user = form.get_user()
            
            auth_login(request, user)
            
            return redirect('prompt')  
        else:
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    

def prompt_view(request):
    if request.method == 'POST':
      
        form = UserCreationForm(request, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')  
        else:
            return redirect('signup')
    else:
        form = LoginForm()
        return render(request, 'signup.html', {'form': form})



    
    
    return render(request, 'prompt.html')
def signup_view(request):
    
    if request.method == 'POST':
      
        form = UserCreationForm(request, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')  
        else:
            return redirect('signup')
    else:
        form = LoginForm()
        return render(request, 'signup.html', {'form': form})

    
    
    







