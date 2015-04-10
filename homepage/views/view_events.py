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
    events = {}
    events['events'] = hmod.Event.objects.all().order_by('name')

    return templater.render_to_response(request, 'view_events.html', events)


@view_function
def order(request):
    events = {}

    if request.urlparams[0] == 'owner':
        order = 'legalEntityID'
    else:
        order = request.urlparams[0]

    events['events'] = hmod.Event.objects.all().order_by(order)

    return templater.render_to_response(request, 'view_events.html', events)

@view_function
def getEventDescription(request):
    data = {}
    data['data'] = hmod.Event.objects.get(entity_ptr_id=request.urlparams[0])
    data['areas'] = hmod.Area.objects.filter(event_id=request.urlparams[0])

    for x in data['areas']:
        x.sale_items = {}
        x.sale_items = hmod.AreaSaleItem.objects.filter(area_id=x.entity_ptr_id)

    return templater.render_to_response(request, 'view_events_modal.html', data)
    # return HttpResponse(data.description)