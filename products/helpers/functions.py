from products.models import VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine, \
    WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee

def print_a():
    print("Hello World")

def list_from_slug(model, slug):
    return model.objects.filter(slug__iexact = slug)

def instance_from_list(filtered_entities):
    for instance in filtered_entities:
        if len(instance) == 1:
            return instance

def get_product_title(slug):
    entities = [
        VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine,
        WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee
    ]
    filtered_entities = []
    for entity in entities:
        filtered_entities.append(list_from_slug(entity, slug))
    
    return instance_from_list(filtered_entities)

# [x.title for x in product_specific("gaggia-classic-pro")][0]

    # return render(
    #     request,
    #     'products/product_specific.html',
    #     {
    #         "object": instance_from_list(filtered_entities),
    #         "DATA_API_KEY":settings.DATA_API_KEY
    #     }
    # )

