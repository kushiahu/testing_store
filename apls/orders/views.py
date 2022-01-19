# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Model
from apls.carts.models import Cart
from apls.orders.models import Order


# Functions Views
@login_required(login_url=reverse_lazy('users:login'))
def order_view(request):

	cart = Cart.objects.filter(user=request.user, status='CR').first()

	order = cart.order if hasattr(cart, 'order') else None

	if order is None:
		order = Order.objects.create(user=request.user, cart=cart)

	order.update_subtotal()

	return render(request, 'orders/confirm.html', {'order': order})


@login_required(login_url=reverse_lazy('users:login'))
def confirm_order(request, id_uuid):
	order = Order.objects.filter(id_uuid=id_uuid).first()
	
	if not order:
		return redirect('book:index')
	
	order.payed()
	request.session['cart_id'] = None
	return redirect('book:index')
