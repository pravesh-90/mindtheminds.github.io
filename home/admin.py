from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm



class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity','issue_by']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name','issue_by',]


# Register your models here.
admin.site.register(Stock,StockCreateAdmin)