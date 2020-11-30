from django.urls import path
from django.contrib.auth import views as auth_views

from payments.views import subscribe, regular_checkout, \
    eduTier1_checkout, eduTier2_checkout, \
    orgTier1_checkout, orgTier2_checkout, \
    stripe_webhook

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('checkout/regular/', regular_checkout, name='regular-checkout'),
    path('checkout/edu-tier-1/', eduTier1_checkout, name='edu1-checkout'),
    path('checkout/edu-tier-2/', eduTier2_checkout, name='edu2-checkout'),
    path('checkout/org-tier-1/', orgTier1_checkout, name='org1-checkout'),
    path('checkout/org-tier-2/', orgTier2_checkout, name='org2-checkout'),
    
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
]