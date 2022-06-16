from django.contrib import admin
from .models import *


# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    list_display = ['code']


admin.site.register(Coupon, CouponAdmin)