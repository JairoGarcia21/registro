from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')
