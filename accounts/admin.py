from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Customer)
# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
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
