from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm




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
      
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')  
        else:
            return redirect('signup')
    else:
        form = LoginForm()
        return render(request, 'signup.html', {'form': form})



    
    
    return render(request, 'prompt.html')



# def signup_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')
    # else:
    #     signup_form = UserCreationForm()
    #     if request.method == 'POST':
    #         signup_form = UserCreationForm(request.POST) 
    #         if signup_form.is_valid():
    #             signup_form.save()
                # messages.success(request,'Account registered successfully.You can login now.')
        #         return redirect('login')
        # context = {'form':signup_form} 
        # return render(request,"app/register.html",context)
    # if request.method == 'POST':
      
    #     form = UserCreationForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
            
    #         return redirect('login')  
    #     else:
    #         return redirect('signup')
    # else:
    #     form = LoginForm()
    #     return render(request, 'signup.html', {'form': form})


def signup_view(request):
    # form_class = UserCreationForm
    # success_url = reverse_lazy('login')
    # template_name = 'signup.html'

    if request.method == 'POST':
      
        form = CustomUserCreationForm(request.POST)
        
        # if form.is_valid():
        form.save()
            
        return redirect('login')  
        # else:
        #     return redirect('signup')
    else:
        form = LoginForm()
        return render(request, 'signup.html', {'form': form})

    
    
    







