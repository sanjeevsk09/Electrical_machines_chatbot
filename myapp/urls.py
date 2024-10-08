"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', account_views.login_view, name='login'),  # Root URL mapped to login_view
    # path('login/', account_views.login_view, name='login'),
    # path('prompt/', account_views.prompt_view, name='prompt'),
    #     # Optional: Separate login path
    #   # Example signup view
    # path('accounts/', include('accounts.urls'))
      # Include the app’s URLs if you have more views
      path("", include("accounts.urls")),
]

