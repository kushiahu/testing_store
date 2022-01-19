import uuid
from django.conf import settings
from django.db import models

# Create your models here.
from apls.books.models import Book


class Cart(models.Model):

	STATUS = (
		('CR', 'CREATED'),
		('CA', 'CANCELED'),
		('CO', 'COMPLETED'),
	)

	id_uuid = models.CharField(default=uuid.uuid4, max_length=36, editable=False)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, related_name='carts',
		on_delete= models.CASCADE, null=True, blank=True
	)
	subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
	total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
	status = models.CharField(max_length=2, choices=STATUS, default='CR')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return owner's cart."""
		return f'Cart of {self.user if self.user else self.id_uuid}'

	def qty_items(self):
		return sum([obj.quantity for obj in self.cart_items.all()])

	def update_total(self):
		self.total = sum([obj.total for obj in self.cart_items.all()])
		self.save()

	def completed(self):
		self.status = 'CO'
		self.save()



class CartItem(models.Model):
	id_uuid = models.CharField(default=uuid.uuid4, max_length=36, editable=False)
	book = models.ForeignKey(Book, related_name='cart_items', on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	quantity = models.PositiveIntegerField(default=1)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return username."""
		return f'Qty: {self.quantity} - {self.book.name}'

	@property
	def total(self):
		return self.price * self.quantity