from django.urls import path

from apls.carts import views

app_name = 'cart'

urlpatterns = [
	path('carrito/', views.cart_view, name="detail"),
	path('add_item/', views.add_item_view, name="add_item"),
]
