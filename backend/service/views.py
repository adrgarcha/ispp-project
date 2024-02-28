from django.shortcuts import render
from .models import Service

# Create your views here.

def list_service(request):
    services = Service.objects.all()
    return render(request, 'services_list.html', {'services': services})