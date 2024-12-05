from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import BookingForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import BookableService
from django.core.paginator import Paginator
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


def services_page(request):
    services = BookableService.objects.all()

    
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if location:
        services = services.filter(location__icontains=location)
    if min_price:
        services = services.filter(price__gte=min_price)
    if max_price:
        services = services.filter(price__lte=max_price)

    paginator = Paginator(services, 6)  # Show 6 services per page
    page_number = request.GET.get('page')  # Get the page number from the GET request
    page_obj = paginator.get_page(page_number)  # Get the page object for the requested page

    return render(request, 'services.html', {'services': services,'page_obj': page_obj})
   