import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse

from apls.carts.models import Cart

# Create your models here.
class Order(models.Model):

	STATUS = (
		('CR', 'CREATED'),
		('PY', 'PAYED'),
		('CP', 'COMPLETED'),
		('CN', 'CANCELED'),
	)

	id_uuid = models.CharField(default=uuid.uuid4, max_length=36, editable=False)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, related_name='orders',
		on_delete= models.CASCADE, null=True, blank=True
	)
	cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='order')
	subtotal = models.DecimalField(default=0, max_digits=12, decimal_places=2) # total carrito
	shipping_total = models.DecimalField(default=0, max_digits=8, decimal_places=2) # Total del envio
	# shipping_address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)
	status = models.CharField(max_length=2, choices=STATUS, default='CR')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'Orden: {self.id_uuid}'

	@property
	def total(self):
		return self.subtotal + self.shipping_total

	def update_subtotal(self):
		self.subtotal = self.cart.total
		self.save()

	def payed(self):
		self.status = 'PY'
		self.cart.completed()
		self.save()

	def get_absolute_url(self):
		return reverse('order:confirm', args=[str(self.id_uuid)])