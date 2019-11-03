from django.shortcuts import render
from .models import Ammonites

# Create your views here.
def all_ammonites(request):
    products = Ammonites.objects.all()
    return render(request, "fossils.html", {"products": products})
