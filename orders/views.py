from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order


def order_confirmation(request, order):
    template_name = 'orders/order_confirmation.html'

    context = {
        'order': order,
    }
    return render(request, template_name, context)


@require_POST
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST)
    user = request.user
    email = user.email

    if form.is_valid():
        print('valid', email)
        order = Order.objects.create(email=email)
        order_id = order.id
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            # очистка корзины
        cart.clear()
    else:
        print(form.errors)

    return HttpResponseRedirect(reverse('orders:order_confirmation', kwargs={'order': order.id}))
