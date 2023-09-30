from curses.ascii import HT
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Car

# Create your views here.

def index(request):
    cars = Car.objects.all()
    return render(request, "index.html", {"cars":cars})

def create(request):
    if request.method == "POST":
        car = Car()
        car.name = request.POST.get('name')
        car.cost = request.POST.get('cost')
        car.save()
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        car = Car.objects.get(id=id)
        if request.method == "POST":
            car.name = request.POST.get('name')
            car.cost = request.POST.get('cost')
            car.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "edit.html", {"car":car})
    except Car.DoesNotExist:
        return HttpResponse('<h1> Car not found </h1>')

def delete(request, id):
    try:
        car = Car.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect('/')
    except Car.DoesNotExist:
        return HttpResponse('<h1> Car not found </h1>')
    
def cost(request):
    cars = Car.objects.all()
    s = 0
    i = 0
    for car in cars:
        s += car.cost
        i += 1
    return HttpResponse(f'<h3> {(s // i)} </h3>')

def prices(request):
    price = request.POST.get('price')
    print(price)
    cars = Car.objects.filter(cost__gt=price)
    return render(request, "price.html", {"cars":cars})