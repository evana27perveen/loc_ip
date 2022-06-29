from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import InformationForm
from geopy.geocoders import Nominatim

# Create your views here.


def home(request):
    form = InformationForm()
    geolocator = Nominatim(user_agent='information')
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            destination_ = form.cleaned_data.get('destination')
            destination = geolocator.geocode(destination_)
            info.destination = destination
            d_lat = destination.latitude
            d_long = destination.longitude
            info.location = "Dhaka"
            info.distance = 5000.00
            # info.save()
    content = {'form': form}
    return render(request, 'app_main/home.html', context=content)

