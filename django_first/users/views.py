from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .form import RegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'forms' : form})



@login_required
def profile(request):
    return render(request,'users/profile.html')


