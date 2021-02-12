from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from django import forms
from .models import VendingMachine, CapsuleMachine, SnackMachine, WaterDispenser, \
    CoffeeBeans, GroundCoffee, CapsuleCoffee, CoffeeMachine

# components = [
#     VendingMachine, CapsuleMachine, SnackMachine,
#     WaterDispenser, CoffeeBeans, GroundCoffee,
#     CapsuleCoffee
# ]

# for component in components:
#     admin.site.register(component)

# After orders
admin.site.unregister(Group)

class LongDescriptionDimensionModifier(forms.ModelForm):

    class Meta:
        fields = "__all__"
        widgets = {
            "long_description": forms.Textarea(
                attrs = {
                    "rows": 10,
                    "cols": 39
                }
            )
        }

# /After orders

##########################################################
# This works
# class LongDescriptionDimensionForm(forms.ModelForm):

#     long_description = forms.CharField(
#         widget = forms.Textarea(
#             attrs = {
#                 "rows":"5",
#                 "cols":"5"
#             }
#         )
#     )
#     class Meta:
#         model = VendingMachine
#         fields = "__all__"

# @admin.register(VendingMachine)
# class CustomVendingMachineAdmin(admin.ModelAdmin):
#     form = LongDescriptionDimensionForm
############################################################

# After orders

@admin.register(VendingMachine)
class CustomVendingMachineAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(CapsuleMachine)
class CustomCapsuleMachineAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(SnackMachine)
class CustomSnackMachineAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(WaterDispenser)
class CustomWaterDispenserAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(CoffeeBeans)
class CustomCoffeeBeansAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(GroundCoffee)
class CustomGroundCoffeeAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(CapsuleCoffee)
class CustomCapsuleCoffeeAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier

@admin.register(CoffeeMachine)
class CustomCoffeeMachineAdmin(admin.ModelAdmin):
    form = LongDescriptionDimensionModifier
# After orders

