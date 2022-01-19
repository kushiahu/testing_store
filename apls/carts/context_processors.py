
from apls.carts.models import Cart


def get_qty_cart(request):
	#request.session['cart_id'] = None
	cart = None
	cart_id = request.session.get('cart_id')
	if request.user.is_authenticated:
		cart = request.user.carts.filter(status='CR').first()
	elif cart_id:
		cart = Cart.objects.filter(id_uuid=cart_id).first()

	return {'pending_cart': cart}