from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

from .forms import Signupform, BlogForm
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# def login(request):
#     name = "login"
#     return render(request, 'myapp/login.html')
#
#
from .models import Blogger


def congo(request):
    return render(request, "myapp/congo.html")


# def signup_view(request):
#     if request.method == "POST":
#         form = forms.Signupform(request.POST)
#         if form.is_valid():
#             # print("first name " + form.cleaned_data['first_name'])
#             # print("last name " + form.cleaned_data['last_name'])
#             # print("pass" + form.cleaned_data['password'])
#             # print("re enter pass " + form.cleaned_data['reenter_password'])
#
#             try:
#                 form.save()
#                 return redirect('login')
#             except:
#                 print("Error saving")
#     else:
#         form = forms.Signupform()
#     return render(request, 'myapp/register.html', {'form': form})


# print(forms.Signupform.cleaned_data['first_name'])


# def Login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             lastname = form.cleaned_data.get('lastname')
#             password = form.cleaned_data.get('password')
#             user = authenticate(lastname=lastname, password=password)
#             if user is not None:
#                 signup_view(request, user)
#                 messages.info(request, f"You are now logged in as {lastname}.")
#                 return redirect("congo")
#             else:
#                 messages.error(request, "Invalid username or password.")
#
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form": form})

#         try:
#             form.save()
#             return redirect('congo')
#         except:
#             print("Error saving")
# else:
#     form = forms.Signupform()
# return render(request, 'myapp/login1.html.html', {'form': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("Hello1")
            messages.success(request, "Registration successful.")
            print("Hello2")
            return redirect(congo)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="myapp/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                print(form)
                return render(request, 'myapp/in.html', {'form': user})
                #return redirect("congo")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="myapp/login.html", context={"login_form": form})


def emp(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'myapp/index.html', {'form': form})


def show(request):
    bloggers = Blogger.objects.all()
    return render(request, 'myapp/show.html', {'bloggers': bloggers})


# DELETE, EDIT/UPDATE
def destroy(request, id):
    blogger = Blogger.objects.get(id=id)
    blogger.delete()
    return redirect('/show')


# UPDATE--> EDIT -> UPDATE
def edit(request, id):
    blogger = Blogger.objects.get(id=id)
    return render(request, 'myapp/edit.html', {'blogger': blogger})


def update(request, id):
    blogger = Blogger.objects.get(id=id)
    form = BlogForm(request.POST, instance=blogger)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'myapp/edit.html', {'blogger': blogger})
