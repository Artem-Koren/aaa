from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
# Create your views here.
def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def debug(request):
    for i in range(100):
        ad = Advertisement(
            title=f"Тестовое объявление {i}",
            text="Текст объявления",
            author="admin"
        )
        ad.save()
        ob = Advertisement.objects.all()
        print(ob)
    return HttpResponse("")