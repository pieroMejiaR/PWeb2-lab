from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinos/destination_list.html', {'destinations': destinations})

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'destinos/add_destination.html', {'form': form})

def update_destination(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destinos/update_destination.html', {'form': form})

def delete_destination(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')
    return render(request, 'destinos/delete_destination.html', {'destination': destination})
