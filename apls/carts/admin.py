from django.contrib import admin

from apls.carts.models import Cart, CartItem


admin.site.register(Cart)
admin.site.register(CartItem)