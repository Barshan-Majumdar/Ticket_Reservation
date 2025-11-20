from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Route
from django.db.models import Q

def landing_page(request):
    return render(request, 'tickets/landing.html')

def login_page(request):
    return render(request, 'tickets/login.html')

def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        request.session['user_profile'] = {
            'name': name,
            'phone': phone,
            'email': email,
        }
        request.session['has_profile'] = True

        return redirect('home')
    return redirect('login')

def home(request):
    return render(request, 'tickets/home.html')

def my_passes(request):
    return render(request, 'tickets/my_passes.html')

def profile(request):
    user_profile = request.session.get('user_profile')
    return render(request, 'tickets/profile.html', {'user_profile': user_profile})

def logout_user(request):
    request.session.flush()
    return redirect('landing')

def station_suggestions(request):
    query = request.GET.get('term', '')
    
    source_stations = Route.objects.values_list('source', flat=True)
    destination_stations = Route.objects.values_list('destination', flat=True)
    
    all_stations = sorted(list(set(list(source_stations) + list(destination_stations))))
    
    if query:
        suggestions = [station for station in all_stations if query.lower() in station.lower()]
    else:
        suggestions = all_stations
        
    return JsonResponse(suggestions, safe=False)

def show_fare(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    try:
        route = Route.objects.get(source__iexact=source, destination__iexact=destination)
        fare = route.price
    except Route.DoesNotExist:
        fare = "Not available"
    return render(request, 'tickets/fare.html', {'source': source, 'destination': destination, 'fare': fare})

def booking_success(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    fare = request.GET.get('fare')
    return render(request, 'tickets/booking_success.html', {'source': source, 'destination': destination, 'fare': fare})