from django.contrib import admin
from guardian.admin import GuardedModelAdmin


from .models import * 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Client)
@admin.register(Order)
class OrderAdmin(GuardedModelAdmin):
    list_display = (
        'status',
        'customer',
    )

    list_filter = (
        "status",
        'customer',
    )

    search_field = (
        'stauts',
        'customer',
    )

    # prepopulated_fields = {
    #     'customer': ('',)
    # } 

    raw_id_fields = ('customer',)
    date_hierarchy = 'date_created'
    ordering = (
        'status',
        'customer',
    )
