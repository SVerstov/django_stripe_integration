import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.contrib import messages

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
domain = settings.DOMAIN

def get_stripe_session_id(request, item_id):
    item = Item.objects.get(pk=item_id)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[

            {
                "price_data": {
                    "currency": item.currency,
                    "product_data": {"name": item.name,
                                     "description": item.description},
                    "unit_amount": int(item.price*100),
                },
                "quantity": 1,
            },

        ],
        mode='payment',
        success_url=domain + f'/success/{item.id}',
        cancel_url=domain + f'/cancel/{item.id}',
    )
    return JsonResponse({'session_id': checkout_session.id})


class ViewItem(DetailView):
    model = Item
    template_name = 'stripe/item.html'




def redirect_to_first_item(request):
    first_item_id = Item.objects.first().pk
    return redirect(f'/item/{first_item_id}')


def success(request, item_id):
    messages.success(request, 'Поздравляем! Вы успешно купили товар!')
    return redirect(f'/item/{item_id}')


def fail(request, item_id):
    messages.error(request, 'Ошибка в оплате, попробуйте ещё раз')
    return redirect(f'/item/{item_id}')

