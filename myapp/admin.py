# myapp/admin.py

from django.contrib import admin
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress, Article, FAQ, Employee
from django.utils import timezone
import pytz

class SaleProductInline(admin.TabularInline):
    model = SaleProduct
    extra = 1

class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleProductInline]

class FAQAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.date_added:
            utc_now = timezone.now()

            local_timezone = pytz.timezone('Europe/Moscow')
            local_now = utc_now.astimezone(local_timezone)

            obj.date_added = local_now

        obj.save()

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale, SaleAdmin)
admin.site.register(CustomerAddress)
admin.site.register(Article)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Employee)
