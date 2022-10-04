from django.shortcuts import render
from django.contrib import messages
from .forms import SignupForm
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Successfully created !!!')
            fm.save()
            fm = SignupForm()
    
    else:
        fm = SignupForm()
    return render (request, 'enroll/signup.html', {'form':fm})