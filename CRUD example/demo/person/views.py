from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from person.models import Person

# Create your views here.
# чтение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people":people})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')

# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "edit.html", {"person":person})
    except Person.DoesNotExist:
        return HttpResponse('<h1> Person not found </h1>')

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponse('<h1> Person not found </h1>')