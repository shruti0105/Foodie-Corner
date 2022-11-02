from django.urls import path
from . import views
from .views import (
    MenuListView,
    menuDetail,
    add_to_cart,
    get_cart_items,
    order_item,
    CartDeleteView,
    order_details,

    add_reviews,
)

app_name = "main"

urlpatterns = [
    path('', MenuListView.as_view(), name='home'),
    path('dishes/<slug>', views.menuDetail, name='dishes'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.get_cart_items, name='cart'),
    path('remove-from-cart/<int:pk>/', CartDeleteView.as_view(), name='remove-from-cart'),
    path('ordered/', views.order_item, name='ordered'),
    path('order_details/', views.order_details, name='order_details'),
    path('postReview', views.add_reviews, name='add_reviews'),
]
