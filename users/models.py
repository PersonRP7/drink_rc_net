from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.utils import IntegrityError
from products.models import VendingMachine, CoffeeMachine, CapsuleMachine, \
        SnackMachine, WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee
from decimal import Decimal



class CustomUser(AbstractUser):

    email = models.EmailField(unique = True)

    class Meta:
        verbose_name_plural = 'Admin panel'

    discount_rates = (
        (0, 0), (5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30),
        (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60),
        (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90),
        (95, 95)

    )

    tax = models.PositiveIntegerField(
        default = 0,
        choices = discount_rates
    )

    def __str__(self):
        return self.username
  

    # @staticmethod
    # def set_discount(user_model_discount, discounted_model):
    #     percentage = CustomUser.objects.get(username = 'admin').user_model_discount
    #     all_products = discounted_model.objects.all()
    #     for product in all_products:
    #         product.price = (percentage / 100) * product.price
    #         product.save()

    # def set_discount(self, which_discount)

    # def set_discount(self, which_discount, which_product):
    #     # Add Exception for products which don't have a set price.
    #     percentage = which_discount
    #     products = which_product.objects.all()
    #     for product in products:
    #         total_discount = (Decimal(percentage) / Decimal(100)) * product.price
    #         if which_discount < Decimal(1):
    #             product.price = product.base_price
    #             product.save()
    #         product.price = product.price - total_discount
    #         product.save()

    def set_discount(self, which_discount, which_product):
        # Add Exception for products which don't have a set price.
        percentage = which_discount
        products = which_product.objects.all()
        try:
            for product in products:
                total_discount = (Decimal(percentage) / Decimal(100)) * product.price
                if which_discount < Decimal(1):
                    product.price = product.base_price
                    product.save()
                product.price = product.price - total_discount
                product.save()
        except TypeError:
            pass


    def save(self, *args, **kwargs):
        if CustomUser.objects.filter(username = "admin"):
            self.set_discount(self.Popust_na_strojeve_na_kovanice, VendingMachine)
            self.set_discount(self.Popust_na_strojeve_za_kavu, CoffeeMachine)
            self.set_discount(self.Popust_na_strojeve_na_kapsule, CapsuleMachine)
            self.set_discount(self.Popust_na_snack_strojeve, SnackMachine)
            self.set_discount(self.Popust_na_vodene_dispenzere, WaterDispenser)
            self.set_discount(self.Popust_na_kavu_u_zrnu, CoffeeBeans)
            self.set_discount(self.Popust_na_mljevenu_kavu, GroundCoffee)
            self.set_discount(self.Popust_na_kapsule_za_nespresso, CapsuleCoffee)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
    


discount_fields = [
    'Popust_na_strojeve_na_kovanice', 'Popust_na_strojeve_na_kapsule',
    'Popust_na_snack_strojeve', 'Popust_na_vodene_dispenzere',
    'Popust_na_kavu_u_zrnu', 'Popust_na_mljevenu_kavu',
    'Popust_na_kapsule_za_nespresso', 'Popust_na_strojeve_za_kavu'
]

for discount_field in discount_fields:
    CustomUser.add_to_class(
        discount_field,
        models.PositiveIntegerField(
            default = 0,
            validators = [
                MinValueValidator(0),
                MaxValueValidator(95)
            ],
            choices = CustomUser.discount_rates
        )
    )