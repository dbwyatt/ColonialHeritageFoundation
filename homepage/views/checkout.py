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
@login_required
def process_request(request):
    items = {}

    return templater.render_to_response(request, 'checkout.html', items)


@view_function
def receipt(request):
    params = {}

    return  templater.render_to_response(request, 'receipt.html', params)