from django.urls import path
from django.contrib.auth import views as auth_views

from payments.views import subscribe, public_checkout, private_checkout, stripe_webhook

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('checkout/public/', public_checkout, name='public-checkout'),
    path('checkout/private/', private_checkout, name='private-checkout'),
    
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
]