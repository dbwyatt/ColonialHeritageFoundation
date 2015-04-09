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
@permission_required('homepage.add_user')
def process_request(request):
    events = {}
    events['events'] = hmod.Event.objects.all().order_by('name')

    return templater.render_to_response(request, 'events.html', events)


@view_function
def edit(request):
    params = {}

    try:
        event = hmod.Event.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    form = EventsForm(initial={
        'name': event.name,
        'description': event.description,
        'startDate': event.startDate,
        'endDate': event.endDate,
        'mapFileName': event.mapFileName,
        'venueName': event.venueName
    })
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.startDate = form.cleaned_data['startDate']
            event.endDate = form.cleaned_data['endDate']
            event.mapFileName = form.cleaned_data['mapFileName']
            event.venueName = form.cleaned_data['venueName']
            event.save()
            return HttpResponseRedirect('/homepage/events/')

    params['form'] = form
    params['events'] = event
    return templater.render_to_response(request, 'events_edit.html', params)


class EventsForm(forms.Form):
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    startDate = forms.DateTimeField(label='Start Date')
    endDate = forms.DateTimeField(label='End Date')
    mapFileName = forms.CharField(label='Map File Name')
    venueName = forms.CharField(label="Venue Name")

    def clean_name(self):
        if len(self.cleaned_data['name']) < 1:
            raise forms.ValidationError('Please enter a name.')
        return self.cleaned_data['name']

    def clean_description(self):
        if len(self.cleaned_data['description']) < 1:
            raise forms.ValidationError('Please enter a description.')
        return self.cleaned_data['description']


@view_function
def create(request):

    params = {}

    form = EventsForm(initial={
        'name': '',
        'description': '',
        'startDate': '',
        'endDate': '',
        'mapFileName': '',
        'venueName': ''
    })
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            event = hmod.Event()
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.startDate = form.cleaned_data['startDate']
            event.endDate = form.cleaned_data['endDate']
            event.mapFileName = form.cleaned_data['mapFileName']
            event.venueName = form.cleaned_data['venueName']
            event.save()
            return HttpResponseRedirect('/homepage/events/')

    params['form'] = form

    return templater.render_to_response(request, 'events_edit.html', params)


@view_function
def delete(request):
    try:
        event = hmod.Event.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    event.delete()
    return HttpResponseRedirect('/homepage/events/')


@view_function
def order(request):
    events = {}

    if request.urlparams[0] == 'owner':
        order = 'legalEntityID'
    else:
        order = request.urlparams[0]

    events['events'] = hmod.Event.objects.all().order_by(order)

    return templater.render_to_response(request, 'events.html', events)