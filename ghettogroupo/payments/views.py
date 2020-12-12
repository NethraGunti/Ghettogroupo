import stripe

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

from users.models import User
from payments.models import Plan, Subscription

stripe.api_key = settings.STRIPE_PRIVATE_KEY
stripe_public_key = settings.STRIPE_PUBLIC_KEY


@login_required
def subscribe(request):
    return render(request, 'payments/plans.html')

@csrf_exempt
def public_checkout(request):
    session = stripe.checkout.Session.create(
        customer_email = request.user.email,
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HxJ0ZD82XqdTEM6WFSgqQN9',
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
def private_checkout(request):
    session = stripe.checkout.Session.create(
        customer_email = request.user.email,
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HxJ2mD82XqdTEM6crO7DRlb',
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
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
    )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    print(event['type'])
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session['customer_email']
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        price_id = line_items['data'][0]['price']['id']

        #price id is of Trial
        if price_id == 'price_1HxJ0ZD82XqdTEM6WFSgqQN9':
            current_plan, created = Plan.objects.get_or_create(
                plan='PUBLIC',
                group_cap = 1,
                member_cap = 20,
                pricing = 50
                )
            if created:
                current_plan.save()


        #price_id is of Diamond
        elif price_id == 'price_1HxJ2mD82XqdTEM6crO7DRlb':
            current_plan, created = Plan.objects.get_or_create(
                plan='PRIVATE',
                group_cap = 1,
                member_cap = 50,
                pricing = 100
                )
            if created:
                current_plan.save()

        new_subscription = Subscription.objects.create(
                            user=User.objects.get(email=customer_email),
                            plan=current_plan,
                            isActive=True)
        new_subscription.save()

    return HttpResponse(status=200)
