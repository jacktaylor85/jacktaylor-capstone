from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import BookingForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import BookableService, Booking
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

def about_us(request):
    return render(request, 'about_us.html')

def login_view(request):
    form = AuthenticationForm()  

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
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

    paginator = Paginator(services, 6)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'services.html', {'services': services,'page_obj': page_obj})
   
@login_required  
def book_service(request, service_id):
    service = get_object_or_404(BookableService, id=service_id)
    total_price = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service  
            booking.user = request.user  

            # Calculate the total price
            duration = (booking.checkout_date - booking.checkin_date).days
            if duration < 1:  # Ensure at least one day is booked
                duration = 1
            total_price = service.price * duration

            booking.save()
            return redirect('profile') 
    else:
        form = BookingForm()

    return render(request, 'book_service.html', {
        'form': form, 
        'service': service, 
        'total_price': total_price,
    })


@login_required
def profile(request):
    user_bookings = request.user.bookings.all()
    return render(request, 'profile.html', {'bookings': user_bookings})


@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(request.user.bookings, id=booking_id)  
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = BookingForm(instance=booking)
    return render(request, 'update_booking.html', {'form': form, 'booking': booking})



@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(request.user.bookings, id=booking_id)
    booking.delete()
    return redirect('profile')