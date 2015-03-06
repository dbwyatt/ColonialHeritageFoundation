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
    areas = {}
    areas['areas'] = hmod.Area.objects.all().order_by('name')

    return templater.render_to_response(request, 'areas.html', areas)


@view_function
def edit(request):
    params = {}

    try:
        area = hmod.Area.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas/')

    form = AreasForm(initial={
        'name': area.name,
        'description': area.description,
        'placeNumber': area.placeNumber,
        'coordinatingAgent': area.coordinatingAgentID.givenName,
        'supervisingAgent': area.supervisingAgentID.givenName,
        'event': area.eventID_id
    })
    if request.method == 'POST':
        form = AreasForm(request.POST)
        if form.is_valid():
            area.name = form.cleaned_data['name']
            area.description = form.cleaned_data['description']
            area.placeNumber = form.cleaned_data['placeNumber']
            area.coordinatingAgentID_id = form.cleaned_data['coordinatingAgent']
            area.supervisingAgentID_id = form.cleaned_data['supervisingAgent']
            area.eventID_id = form.cleaned_data['event']
            area.save()
            return HttpResponseRedirect('/homepage/areas/')

    params['form'] = form
    params['areas'] = area
    return templater.render_to_response(request, 'items_edit.html', params)


class AreasForm(forms.Form):
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    placeNumber = forms.DecimalField(label='Place Number')
    coordinatingAgent = forms.ChoiceField(label='Coordinating Agent', choices=[(x.entity_ptr_id, x.givenName) for x in hmod.Agent.objects.all()])
    supervisingAgent = forms.ChoiceField(label='Supervising Agent', choices=[(x.entity_ptr_id, x.givenName) for x in hmod.Agent.objects.all()])
    event = forms.ChoiceField(label='Event', choices=[(x.entity_ptr_id, x.name) for x in hmod.Event.objects.all()])

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

    form = AreasForm(initial={
        'name': '',
        'description': '',
        'placeNumber': '',
        'coordinatingAgent': '',
        'supervisingAgent': '',
        'event': ''
    })
    if request.method == 'POST':
        form = AreasForm(request.POST)
        if form.is_valid():
            area = hmod.Area()
            area.name = form.cleaned_data['name']
            area.description = form.cleaned_data['description']
            area.placeNumber = form.cleaned_data['placeNumber']
            area.coordinatingAgentID_id = form.cleaned_data['coordinatingAgent']
            area.supervisingAgentID_id = form.cleaned_data['supervisingAgent']
            area.eventID_id = form.cleaned_data['event']
            area.save()
            return HttpResponseRedirect('/homepage/areas/')

    params['form'] = form

    return templater.render_to_response(request, 'items_edit.html', params)


@view_function
def delete(request):
    try:
        area = hmod.Area.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas/')

    area.delete()
    return HttpResponseRedirect('/homepage/areas/')


@view_function
def order(request):
    areas = {}

    if request.urlparams[0] == 'owner':
        order = 'legalEntityID'
    else:
        order = request.urlparams[0]

    areas['areas'] = hmod.Area.objects.all().order_by(order)

    return templater.render_to_response(request, 'areas.html', areas)