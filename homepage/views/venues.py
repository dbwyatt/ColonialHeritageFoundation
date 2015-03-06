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
    venues = {}
    venues['venues'] = hmod.Venue.objects.all().order_by('name')

    return templater.render_to_response(request, 'venues.html', venues)


@view_function
def edit(request):
    params = {}

    try:
        venue = hmod.Venue.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/homepage/venues/')

    form = VenuesForm(initial={
        'name': venue.name,
        'address': venue.address,
        'city': venue.city,
        'state': venue.state,
        'zip': venue.zip
    })
    if request.method == 'POST':
        form = VenuesForm(request.POST)
        if form.is_valid():
            venue.name = form.cleaned_data['name']
            venue.address = form.cleaned_data['address']
            venue.city = form.cleaned_data['city']
            venue.state = form.cleaned_data['state']
            venue.zip = form.cleaned_data['zip']
            venue.save()
            return HttpResponseRedirect('/homepage/venues/')

    params['form'] = form
    params['venues'] = venue
    return templater.render_to_response(request, 'venues_edit.html', params)


class VenuesForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    state = forms.CharField(label='State')
    zip = forms.CharField(label='Zip Code')

    def clean_name(self):
        if len(self.cleaned_data['name']) < 1:
            raise forms.ValidationError('Please enter a name.')
        return self.cleaned_data['name']


@view_function
def create(request):

    params = {}

    form = VenuesForm(initial={
        'name': '',
        'address': '',
        'city': '',
        'state': '',
        'zip': '',
    })
    if request.method == 'POST':
        form = VenuesForm(request.POST)
        if form.is_valid():
            venue = hmod.Venue()
            venue.name = form.cleaned_data['name']
            venue.address = form.cleaned_data['address']
            venue.city = form.cleaned_data['city']
            venue.state = form.cleaned_data['state']
            venue.zip = form.cleaned_data['zip']
            venue.save()
            return HttpResponseRedirect('/homepage/venues/')

    params['form'] = form

    return templater.render_to_response(request, 'venues_edit.html', params)


@view_function
def delete(request):
    try:
        venue = hmod.Venue.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.DoesNotExist:
        return HttpResponseRedirect('/homepage/venues/')

    venue.delete()
    return HttpResponseRedirect('/homepage/venues/')


@view_function
def order(request):
    venues = {}

    if request.urlparams[0] == 'owner':
        order = 'legalEntityID'
    else:
        order = request.urlparams[0]

    venues['venues'] = hmod.Venue.objects.all().order_by(order)

    return templater.render_to_response(request, 'venues.html', venues)