from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from panel.models import Person
# Create your views here.
def home(request):
    if request.POST:
        person = Person(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'])
        person.save()
        import pdb
        pdb.set_trace()
    return render(request, 'panel/home.html', locals())


def list(request):
    persons = Person.objects.all()
    return render(request, 'panel/list.html', locals())
 
def edit(request, pk):
    
    person = Person.objects.filter(pk= pk).first() # get(pk)
    if request.POST:
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.email = request.POST['email']
        person.save()
    return render(request, 'panel/home.html', locals())

def delete(request, pk): 
    person = Person.objects.get(pk = pk) # get(pk)
    person.delete()
    return redirect(reverse('panel:list'))