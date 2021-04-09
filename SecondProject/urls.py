"""SecondProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login', views.login, name='login'),
    path('congo', views.congo, name='congo'),
    # path('register', views.signup_view, name="register"),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name='login'),
    path('emp', views.emp),
    path('show', views.show, name='show'),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    # path("register", views.register_request, name="register")
]
