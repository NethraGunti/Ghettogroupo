from django.urls import path
from django.contrib.auth import views as auth_views

from payments.views import subscribe, regular_checkout, \
    eduTier1_checkout, eduTier2_checkout, \
    orgTier1_checkout, orgTier2_checkout, \
    stripe_webhook

urlpatterns = [
    path('', subscribe, name='regular'),
    path('regular/', regular_checkout, name='regular-checkout'),
    path('edu-tier-1/', eduTier1_checkout, name='edu1-checkout'),
    path('edu-tier-2/', eduTier2_checkout, name='edu2-checkout'),
    path('org-tier-1/', orgTier1_checkout, name='org1-checkout'),
    path('org-tier-2/', orgTier2_checkout, name='stripe_webhook'),
    
    path('stripe_webhook/', stripe_webhook, name='org2-checkout'),
]