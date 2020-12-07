import stripe

from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

from payments.models import Plan, Subscription

stripe.api_key = settings.STRIPE_PRIVATE_KEY
stripe_public_key = settings.STRIPE_PUBLIC_KEY


def subscribe(request):
    user = request.user
    if user.is_authenticated:
        if Subscription.objects.filter(user=user):
            subscription = Subscription.objects.get(user=user, isActive=True)
            if subscription.isActive:
                return redirect(reverse_lazy('landing-page'))
        return render(request, 'payments/plans.html')
    return redirect(reverse_lazy('login'))

@csrf_exempt
def regular_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Hmf2VD82XqdTEM6FbWm7KsD',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('landing-page')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing-page')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : stripe_public_key
    })


@csrf_exempt
def eduTier1_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Hmcm8D82XqdTEM6JaQhO0F4',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('landing-page')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing-page')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : stripe_public_key
    })

@csrf_exempt
def eduTier2_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HmcmZD82XqdTEM6I2Ot89OI',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('landing-page')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing-page')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : stripe_public_key
    })

@csrf_exempt
def orgTier1_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HmcmsD82XqdTEM63waaZi2h',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('landing-page')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing-page')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : stripe_public_key
    })


@csrf_exempt
def orgTier2_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HmcnKD82XqdTEM6gLROMdOd',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('landing-page')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing-page')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : stripe_public_key
    })


@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = 'whsec_Tj6LmBopa0xZpIqLd3S3oJuuzKA6N8M2'
    payload = request.body
    slg_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, slg_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'payment_intent.completed':
        session = event['data']['object']
        payment_intent = event.data.object # contains a stripe.PaymentIntent
    #     print('PaymentIntent was successful!')
    # elif event.type == 'payment_method.attached':
    #     payment_method = event.data.object # contains a stripe.PaymentMethod
    #     print('PaymentMethod was attached to a Customer!')
    # # ... handle other event types
    # else:
    # print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
