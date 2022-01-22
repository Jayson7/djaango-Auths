from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms  import forms, UserCreationForm
# Create your views here.


def Homepage(request):
    
    return render(request, 'index.html')


def  register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user 
            user_info.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
        

    context = {'form' : form}

    return render(request, 'registration/register.html', context)

    