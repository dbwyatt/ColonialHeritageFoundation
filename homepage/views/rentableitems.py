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
    items = {}
    items['items'] = hmod.Item.objects.all().order_by('name')

    return templater.render_to_response(request, 'rentableitems.html', items)


@view_function
def edit(request):
    params = {}

    try:
        item = hmod.Item.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentableitems/')

    form = ItemEditForm(initial={
        'name': item.name,
        'description': item.description,
        'value': item.value,
        'standardRentalPrice': item.standardRentalPrice,
        'owner': item.legalEntityID_id,
    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['rentable'] == True:
                rentable = hmod.RentableItem()
                rentable.name = form.cleaned_data['name']
                rentable.description = form.cleaned_data['description']
                rentable.value = form.cleaned_data['value']
                rentable.standardRentalPrice = form.cleaned_data['standardRentalPrice']
                rentable.legalEntityID_id = form.cleaned_data['owner']
                rentable.save()
                return HttpResponseRedirect('/homepage/rentableitems/')

    params['form'] = form
    params['items'] = item
    return templater.render_to_response(request, 'items_edit.html', params)


class ItemEditForm(forms.Form):
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    value = forms.DecimalField(label='Value')
    standardRentalPrice = forms.DecimalField(label='Standard Rental Price')
    owner = forms.ChoiceField(label='Owner', choices=[(x.entity_ptr_id, x.givenName) for x in hmod.LegalEntity.objects.all()])
    rentable = forms.CharField(widget=forms.CheckboxInput)

    def clean_name(self):
        if len(self.cleaned_data['name']) < 1:
            raise forms.ValidationError('Please enter a name.')
        return self.cleaned_data['name']

    def clean_description(self):
        if len(self.cleaned_data['description']) < 1:
            raise forms.ValidationError('Please enter a description.')
        return self.cleaned_data['description']

    def clean_value(self):
        if self.cleaned_data['value'] < 0:
            raise forms.ValidationError('Please enter a value.')
        return self.cleaned_data['value']

    def clean_standardRentalPrice(self):
        if self.cleaned_data['standardRentalPrice'] < 1:
            raise forms.ValidationError('Please enter a rental price.')
        return self.cleaned_data['standardRentalPrice']


@view_function
def create(request):

    params = {}

    form = ItemEditForm(initial={
        'name': '',
        'description': '',
        'value': '',
        'standardRentalPrice': '',
        'owner': '',
    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            item = hmod.Item()
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.standardRentalPrice = form.cleaned_data['standardRentalPrice']
            item.legalEntityID_id = form.cleaned_data['owner']
            item.save()
            return HttpResponseRedirect('/homepage/items/')

    params['form'] = form

    return templater.render_to_response(request, 'items_edit.html', params)


@view_function
def delete(request):
    try:
        item = hmod.Item.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.DoesNotExist:
        return HttpResponseRedirect('/homepage/items/')

    item.delete()
    return HttpResponseRedirect('/homepage/items/')


@view_function
def order(request):
    items = {}

    if request.urlparams[0] == 'owner':
        order = 'legalEntityID'
    else:
        order = request.urlparams[0]

    items['items'] = hmod.Item.objects.all().order_by(order)

    return templater.render_to_response(request, 'items.html', items)