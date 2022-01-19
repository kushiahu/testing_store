from django.urls import path

from apls.orders import views

app_name = 'order'

urlpatterns = [	
	path('orden/', views.order_view, name="detail"),
	path('orden/confirm/<uuid:id_uuid>/', views.confirm_order, name='confirm'),
]
