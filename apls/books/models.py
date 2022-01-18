import uuid

from django.db import models
from django.template.defaultfilters import slugify



# Models
class Editorial(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name



class Author(models.Model):
	name = models.CharField(max_length=120)
	country = models.CharField(max_length=80)

	def __str__(self):
		return self.name



class Book(models.Model):

	LENGUAGE = (
		('es', 'Español'),
		('en', 'Ingles'),
	)

	BINDING = (
		('TN', 'Tapa normal'),
		('TP', 'Tapa dura'),
	)

	id_uuid = models.CharField(default=uuid.uuid4, max_length=36, editable=False)
	slug = models.SlugField(unique=True, editable=False)
	name = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to='books/')
	page_numbers = models.PositiveIntegerField(default=0)
	year_publication = models.DateField(null=True, blank=True)
	lenguage = models.CharField(max_length=2, choices=LENGUAGE, default='es')
	book_binding = models.CharField(max_length=2, choices=BINDING, default='TN')
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	stock = models.PositiveIntegerField(default=0)

	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
	editorials = models.ManyToManyField(Editorial, related_name='books')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name) + '-' +  str(uuid.uuid4()).split('-')[0]
		super(Book, self).save(*args, **kwargs)
