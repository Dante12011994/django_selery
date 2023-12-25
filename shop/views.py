from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
import stripe

from shop.models import Item


class ItemDetailView(DetailView):
    model = Item


class ItemListView(ListView):
    model = Item


def buy(request, pk):
    stripe.api_key = settings.STRIPE_API_KEY

    item = get_object_or_404(Item, pk=pk)
    price = stripe.Price.create(
        currency="usd",
        unit_amount=item.price,
        product_data={"name": item.name},
    )
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000",
        line_items=[{"price": price['id'], "quantity": 1}],
        mode="payment",
    )
    context = {'session': session}
    return render(request, 'shop/buy.html', context)
