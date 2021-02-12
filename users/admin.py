from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

admin.site.site_header = 'Promet Aroma Admin'
admin.site.site_title = 'Promet Aroma'
admin.site.index_title = 'Promet Aroma Inventar'

# admin.site.register(CustomUser)
class DoNotLog:
    def log_addition(self, *args):
        pass

    def log_change(self, *args):
        pass

    def log_deletion(self, *args):
        pass

# class CustomUserAdmin(UserAdmin):
#     # This works, but also shows other fields
#     fieldsets = (
#         *UserAdmin.fieldsets,  # original form fieldsets, expanded
#         (                      # new fieldset added on to the bottom
#             'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
#             {
#                 'fields': (
#                     'Popust_na_strojeve_za_kavu',
#                 ),
#             },
#         ),
#     )

class CustomUserAdmin(DoNotLog, UserAdmin):
    # This works, but also shows other fields

    fieldsets = (
        (                      # new fieldset added on to the bottom
            'Popusti',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'Popust_na_strojeve_na_kovanice', 'Popust_na_strojeve_na_kapsule',
    'Popust_na_snack_strojeve', 'Popust_na_vodene_dispenzere',
    'Popust_na_kavu_u_zrnu', 'Popust_na_mljevenu_kavu',
    'Popust_na_kapsule_za_nespresso', 'Popust_na_strojeve_za_kavu',
                ),
            },
        ),
    )

    MAX_OBJECTS = 1

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(CustomUser, CustomUserAdmin)


