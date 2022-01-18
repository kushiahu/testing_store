from django.urls import path

from apls.books import views


app_name = 'book'

urlpatterns = [
    path('', views.book_index, name='index'),
    path('libro/<slug:slug>/', views.detail_view, name='detail'),
]