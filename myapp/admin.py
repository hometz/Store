# myapp/admin.py

from django.contrib import admin
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress, Article, FAQ, Employee, PromoCode
from django.utils import timezone
import pytz

class SaleProductInline(admin.TabularInline):
    model = SaleProduct
    extra = 1

class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleProductInline]

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale, SaleAdmin)
admin.site.register(CustomerAddress)
admin.site.register(Article)
admin.site.register(Employee)
admin.site.register(PromoCode)
admin.site.register(FAQ)
