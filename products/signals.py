# from django.db.models.signals import pre_save
# from django.db.models.signals import post_save
# from django.utils.text import slugify
# # from django.dispatch import receiver
# from .models import VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine, WaterDispenser, \
#     CoffeeBeans, GroundCoffee, CapsuleCoffee

# data_models = [
#     VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine, WaterDispenser,
#     CoffeeBeans, GroundCoffee, CapsuleCoffee
# ]

# def add_slug(sender, **kwargs):
#     instance = kwargs['instance']
#     instance.slug = slugify(instance.title)

# for data_model in data_models:
#     post_save.connect(add_slug, sender = data_model)
