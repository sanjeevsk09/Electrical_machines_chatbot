# myapp/urls.py
from django.urls import path
from .views import login_view
from.views import prompt_view
from.views import signup_view
from django.contrib import admin



urlpatterns = [
    path('', login_view, name='login'),
    path('admin/',admin.site.urls),
    path('login/', login_view, name='login'),
    path('prompt/', prompt_view, name='prompt'),
    path('signup/', signup_view, name='signup')

    
]
