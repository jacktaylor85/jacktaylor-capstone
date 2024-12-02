from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import BookingForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home or any other page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})