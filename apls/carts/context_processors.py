
from apls.carts.models import Cart


def get_qty_cart(request):
	#request.session['cart_id'] = None
	cart = None
	cart_id = request.session.get('cart_id')

	if cart_id and request.user.is_authenticated:
		cart = Cart.objects.filter(id_uuid=cart_id, status='CR').first()
		if not cart.user:
			cart.user = request.user
			cart.save()
			request.session['cart_id'] = None
	elif request.user.is_authenticated:
		cart = request.user.carts.filter(status='CR').first()
	elif cart_id:
		cart = Cart.objects.filter(id_uuid=cart_id).first()

	return {'pending_cart': cart}