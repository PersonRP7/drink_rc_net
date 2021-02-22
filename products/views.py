from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from itertools import chain
from .models import VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine, \
    WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee
from .forms import SearchForm
from django.urls import reverse

from django.conf import settings

# New addition
from products.helpers.functions import get_product_title
#/New addition


# Outside of products:
# VendingMachines, CapsuleMachine, SnackMachine, WaterDispenser


def list_from_slug(model, slug):
    return model.objects.filter(slug__iexact = slug)

def instance_from_list(filtered_entities):
    for instance in filtered_entities:
        if len(instance) == 1:
            return instance


def product_specific(request, slug):
    entities = [
        VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine,
        WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee
    ]
    filtered_entities = []
    for entity in entities:
        filtered_entities.append(list_from_slug(entity, slug))

    return render(
        request,
        'products/product_specific.html',
        {
            "object": instance_from_list(filtered_entities),
            #New addition
            "title": [x.title for x in get_product_title(slug)][0],
            #/New addition
            "DATA_API_KEY":settings.DATA_API_KEY
        }
    )

def all_links(request):
    coffee_machines = CoffeeMachine.objects.all()
    coffee_beans = CoffeeBeans.objects.all()
    ground_coffee = GroundCoffee.objects.all()
    capsule_coffee = CapsuleCoffee.objects.all()
    products = list(chain(coffee_machines, coffee_beans, ground_coffee, capsule_coffee))
    return render(
        request,
        'products/all_links.html',
        {
            "products":products
        }
    )

def full_urls(request):
    coffee_machines = CoffeeMachine.objects.all()
    coffee_beans = CoffeeBeans.objects.all()
    ground_coffee = GroundCoffee.objects.all()
    capsule_coffee = CapsuleCoffee.objects.all()
    products = list(chain(coffee_machines, coffee_beans, ground_coffee, capsule_coffee))
    return render(
        request,
        'products/full_urls.html',
        {
            "products":products
        }
    )


def products_all(request):
    coffee_machines = CoffeeMachine.objects.all()
    coffee_beans = CoffeeBeans.objects.all()
    ground_coffee = GroundCoffee.objects.all()
    capsule_coffee = CapsuleCoffee.objects.all()
    products = list(chain(coffee_machines, coffee_beans, ground_coffee, capsule_coffee))
    return render(
        request,
        'products/all.html',
        {
            "products":products,
            "DATA_API_KEY":settings.DATA_API_KEY
        }
    )

def search(request):
    if request.method == 'GET':
        form = SearchForm()
        return render(
            request, 'products/search.html', {"form":form}
        )
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get("search")
            return HttpResponseRedirect(
                reverse('products:search_data', kwargs = {"query": data})
            )
        else:
            return render(request, 'products/search.html')


def search_data(request, query):
    coffee_machines = CoffeeMachine.objects.filter(slug__contains = query)
    coffee_beans = CoffeeBeans.objects.filter(slug__contains = query)
    ground_coffee = GroundCoffee.objects.filter(slug__contains = query)
    capsule_coffee = CapsuleCoffee.objects.filter(slug__contains = query)
    products = list(chain(coffee_machines, coffee_beans, ground_coffee, capsule_coffee))
    return render(request, 'products/search_data.html', {"products": products})



# Use get_object_or_404 here.
def coffee_sort(request, title):
    if title == "beans":
        products = CoffeeBeans.objects.all()
        return render(
            request, 'products/coffee_sort.html',
            {"products":products, "DATA_API_KEY":settings.DATA_API_KEY}
        )
    elif title == "ground":
        products = GroundCoffee.objects.all()
        return render(
            request, 'products/coffee_sort.html',
            {"products":products, "DATA_API_KEY":settings.DATA_API_KEY}
        )
    elif title == "capsule":
        products = CapsuleCoffee.objects.all()
        return render(
            request, 'products/coffee_sort.html',
            {"products":products, "DATA_API_KEY":settings.DATA_API_KEY}
        )

def coffee_overview(request):
    return render(
        request,
        'products/coffee_overview.html'
    )

def machine_overview(request):
    return render(
        request,
        'products/machine_overview.html'
    )

def vending_machine(request):
    return render(
        request,
        'products/vending_machine.html'
    )

def capsule_machine(request):
    return render(
        request,
        'products/capsule_machine.html'
    )

def snack_machine(request):
    return render(
        request,
        'products/snack_machine.html'
    )

def water_dispenser(request):
    return render(
        request,
        'products/water_dispenser.html'
    )









#
