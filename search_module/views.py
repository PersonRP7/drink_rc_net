from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from itertools import chain
from products.models import VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine, \
    WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee
from .forms import SearchForm
from django.urls import reverse

def search_module_view(request):
    return HttpResponse("This is the search module view.")

def search(request):
    if request.method == 'GET':
        form = SearchForm()
        return render(
            request, 'search_module/search.html', {"form":form}
        )
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get("search")
            return HttpResponseRedirect(
                reverse('search_module:search_data', kwargs = {"query": data})
            )
        else:
            return render(request, 'search_module/search.html')


def search_data(request, query):
    coffee_machines = CoffeeMachine.objects.filter(title__contains = query)
    coffee_beans = CoffeeBeans.objects.filter(title__contains = query)
    ground_coffee = GroundCoffee.objects.filter(title__contains = query)
    capsule_coffee = CapsuleCoffee.objects.filter(title__contains = query)
    products = list(chain(coffee_machines, coffee_beans, ground_coffee, capsule_coffee))
    return render(request, 'search_module/search_data.html', {"products": products})

