__author__ = 'Daniel'

from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required, login_required

templater = get_renderer('homepage')


@view_function
def process_request(request):
    items = {}

    return templater.render_to_response(request, 'product.html', items)


@view_function
def updatecart(request):
    item = {}
    item['id'] = request.urlparams[0]
    item['quantity'] = request.urlparams[1]

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    # If item.id is already in shopping_cart, increment it by qty added, otherwise, set item.id as qty added
    if item['id'] in request.session['shopping_cart']:
        request.session['shopping_cart'][item['id']] = int(item['quantity'])
    else:
        request.session['shopping_cart'][item['id']] = int(item['quantity'])

    request.session.modified = True

    return HttpResponseRedirect('/homepage/product/')


@view_function
def updatecartadd(request):
    if request.user.is_authenticated():
        item = {}
        item['id'] = request.urlparams[0]
        item['quantity'] = request.urlparams[1]

        if 'shopping_cart' not in request.session:
            request.session['shopping_cart'] = {}

        # If item.id is already in shopping_cart, increment it by qty added, otherwise, set item.id as qty added
        if item['id'] in request.session['shopping_cart']:
            request.session['shopping_cart'][item['id']] += int(item['quantity'])
        else:
            request.session['shopping_cart'][item['id']] = int(item['quantity'])

        request.session.modified = True

        return HttpResponse("Updated")

    else:
        return HttpResponse("Login")


@view_function
def getcart(request):
    cart = {}

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    cart['items'] = hmod.Item.objects.filter(entity_ptr_id__in=request.session['shopping_cart'].keys())
    cart['cart'] = request.session['shopping_cart']

    for x in cart['items']:
        print("key: {}".format(x.entity_ptr_id))
        print(cart['cart'][str(x.entity_ptr_id)])
        x.shopping_cart_quantity = cart['cart'][str(x.entity_ptr_id)]
        print(x.shopping_cart_quantity)

    for x, y in cart['cart'].items():
        # print(cart['items'][x])
        print("key: {}, value: {}".format(x, y))
    # for x in cart['items']:

    return templater.render_to_response(request, "cart.html", cart)


@view_function
def rentupdatecart(request):
    if request.user.is_authenticated():
        item = {}
        item['id'] = request.urlparams[0]
        item['quantity'] = request.urlparams[1]

        if 'shopping_cart' not in request.session:
            request.session['shopping_cart'] = {}

        # If item.id is already in shopping_cart, increment it by qty added, otherwise, set item.id as qty added
        if item['id'] in request.session['shopping_cart']:
            return HttpResponse(False)
        else:
            request.session['shopping_cart'][item['id']] = int(item['quantity'])

        request.session.modified = True

        return HttpResponse("Updated")

    else:
        return HttpResponse("Login")


@view_function
def delete(request):

    del request.session['shopping_cart'][str(request.urlparams[0])]
    request.session.modified = True

    return HttpResponse("Deleted")