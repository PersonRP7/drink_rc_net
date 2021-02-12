from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from itertools import chain

# class AbstractOverview(models.Model):

#     class Meta:
#         abstract = True

#     title = models.CharField(max_length = 200)
#     code = models.CharField(max_length = 200)
#     cover = models.ImageField(
#         upload_to = 'images/'
#     )

#     def __str__(self):
#         return self.title

# class CoffeeOverview(AbstractOverview):
#     pass

# class MachineOverview(AbstractOverview):
#     pass
    

class ProductsAbstract(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(max_length = 100)
    short_description = models.CharField(max_length = 250)
    long_description = models.CharField(max_length = 2000)
    heading_1 = models.CharField(max_length = 200, blank = True, null = True)
    heading_2 = models.CharField(max_length = 200, blank = True, null = True)
    heading_3 = models.CharField(max_length = 200, blank = True, null = True)
    heading_4 = models.CharField(max_length = 200, blank = True, null = True)
    heading_5 = models.CharField(max_length = 200, blank = True, null = True)
    heading_6 = models.CharField(max_length = 200, blank = True, null = True)
    heading_7 = models.CharField(max_length = 200, blank = True, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2,
        blank = True, null = True 
    )
    base_price = models.DecimalField(max_digits = 6, decimal_places = 2,
        blank = True, null = True
    )
    cover = models.ImageField(
        upload_to = 'images/'
    )
    slug = models.SlugField(
        max_length = 100,
        unique = True,
        blank = True,
        null = True
    )

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)

    #     super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.price > 0:
    #         self.base_price = self.price
    #     if not self.slug:
    #         self.slug = slugify(self.title)

    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        if self.base_price == None:
            self.base_price = self.price
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:product_specific", kwargs={"slug": self.slug})
    

class VendingMachine(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Strojevi na kovanice'

    # def get_absolute_url(self):
    #     return reverse("products:vending_machines")

class CoffeeMachine(ProductsAbstract):

    class Meta:
        verbose_name_plural = "Strojevi za kavu"

class CapsuleMachine(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Strojevi na kapsule'

    # def get_absolute_url(self):
    #     return reverse("products:capsule_machines")

class SnackMachine(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Snack strojevi'

    # def get_absolute_url(self):
    #     return reverse("products:snack_machines")

class WaterDispenser(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Vodeni dispenzeri'

    # def get_absolute_url(self):
    #     return reverse("products:water_dispensers")

class CoffeeBeans(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Kava u zrnu'

    # def get_absolute_url(self):
    #     return reverse("products:coffee_beans")

class GroundCoffee(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Mljevena kava'

    # def get_absolute_url(self):
    #     return reverse("products:ground_coffee")

class CapsuleCoffee(ProductsAbstract):

    class Meta:
        verbose_name_plural = 'Kapsule na nespresso'

    # def get_absolute_url(self):
    #     return reverse("products:capsule_coffee")
    
    
def remove_all():
    from products.models import VendingMachine, CoffeeMachine, CapsuleMachine, \
        SnackMachine, WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee

    instances = [
        VendingMachine, CoffeeMachine, CapsuleMachine,
        SnackMachine, WaterDispenser, CoffeeBeans, GroundCoffee,
        CapsuleCoffee
    ]

    for instance in instances:
        instance.objects.all().delete()

def add_slugs():
    # This works
    from products.models import VendingMachine, CoffeeMachine, CapsuleMachine, \
        SnackMachine, WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee

    instances = [
        VendingMachine.objects.all(), CoffeeMachine.objects.all(), CapsuleMachine.objects.all(),
        SnackMachine.objects.all(), WaterDispenser.objects.all(), CoffeeBeans.objects.all(), GroundCoffee.objects.all(),
        CapsuleCoffee.objects.all()
    ]

    for instance in instances:
        for i in instance:
            i.save()

def instance_from_slug(model, slug):
    return model.objects.filter(slug__iexact = slug)

def product_specific(slug):
    from products.models import VendingMachine, CoffeeMachine, CapsuleMachine, \
        SnackMachine, WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee

    entities = [
        VendingMachine, CoffeeMachine, CapsuleMachine, SnackMachine,
        WaterDispenser, CoffeeBeans, GroundCoffee, CapsuleCoffee
    ]
    filtered_entities = []
    for entity in entities:
        filtered_entities.append(instance_from_slug(entity, slug))
    return filtered_entities

def resize_on_upload(name):
    from PIL import Image
    img = Image.open(f"./{name}")
    output_size = (800, )
    img.thumbnail(output_size)
    img.save(f"./{name}")


def r(name):
    from PIL import Image
    img = Image.open(f"./{name}")
    img2 = img.resize((400, 400), Image.LANCZOS)
    img2.save(f"{name}", optimize = True)


    
    
# def mymodel_pre_save(sender, **kwargs):
#     instance = kwargs['instance']
#     instance.slug = slugify(instance.name)

# pre_save.connect(mymodel_pre_save, sender=MyModel)
    
# >>> def search(model):
# ...     return model.objects.filter(slug__iexact = object.slug)
# ...
# >>> search(CoffeeMachine)
# <QuerySet [<CoffeeMachine: Coffee Machine 1>]>
# >>> search(CoffeeBeans)
# <QuerySet []>
# >>> entities = [CoffeeMachine, CoffeeBeans]
# >>> for entity in entities:
# ...     search(entity)
# ...
# <QuerySet [<CoffeeMachine: Coffee Machine 1>]>
# <QuerySet []>