__author__ = 'ryan'

from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO

templater = get_renderer('homepage')


@view_function
def process_request(request):
    items = {}
    item_spec = hmod.ItemSpecifications.objects.filter(name__icontains=request.urlparams[0])
    items['items'] = hmod.Item.objects.filter(itemSpecifications__in=item_spec)

    items['events'] = hmod.Event.objects.filter(name__icontains=request.urlparams[0])


    # items['items'] = hmod.Item.objects.all().order_by('itemSpecifications__name')
    # items['events'] = hmod.Event.objects.all().order_by('name')

    return templater.render_to_response(request, 'search.html', items)