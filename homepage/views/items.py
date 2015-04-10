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
    items['items'] = hmod.Item.objects.all().order_by('itemSpecifications__name')

    return templater.render_to_response(request, 'items.html', items)


@view_function
@permission_required('homepage.add_user')
def edit(request):
    params = {}

    try:
        item = hmod.Item.objects.get(entity_ptr_id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/items/')

    form = ItemEditForm(initial={
        'name': item.itemSpecifications.name,
        'description': item.itemSpecifications.description,
        'price': item.itemSpecifications.price,
        'owner': item.itemSpecifications.user.first_name + item.itemSpecifications.user.last_name,
        'cost': item.cost,
        'quantityOnHand': item.quantityOnHand,
        'forSale': item.forSale
    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            itemSpec = item.itemSpecifications
            itemSpec.name = form.cleaned_data['name']
            itemSpec.description = form.cleaned_data['description']
            itemSpec.user_id = form.cleaned_data['owner']
            itemSpec.price = form.cleaned_data['price']
            item.cost = form.cleaned_data['cost']
            if form.cleaned_data['forSale'] == 'True':
                item.forSale = True
            elif form.cleaned_data['forSale'] == 'False':
                item.forSale = False
            item.quantityOnHand = form.cleaned_data['quantityOnHand']
            item.save(force_update=True)
            return HttpResponseRedirect('/homepage/items/')

    params['form'] = form
    params['items'] = item
    return templater.render_to_response(request, 'items_edit.html', params)


class ItemEditForm(forms.Form):
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    price = forms.CharField(label='Price')
    owner = forms.ChoiceField(label='Owner', choices=[(x.id, x.first_name + ' ' + x.last_name) for x in hmod.User.objects.all()])
    cost = forms.CharField(label='Cost')
    quantityOnHand = forms.CharField(label='Quantity on Hand')
    forSale = forms.ChoiceField(label='For Sale', choices=(('True', 'Yes'), ('False', 'No')))

    def clean_name(self):
        if len(self.cleaned_data['name']) < 1:
            raise forms.ValidationError('Please enter a name.')
        return self.cleaned_data['name']

    def clean_description(self):
        if len(self.cleaned_data['description']) < 1:
            raise forms.ValidationError('Please enter a description.')
        return self.cleaned_data['description']

    def clean_price(self):
        if float(self.cleaned_data['price']) < 0:
            raise forms.ValidationError('Please enter a value.')
        return self.cleaned_data['price']

    def clean_cost(self):
        if float(self.cleaned_data['cost']) < 0:
            raise forms.ValidationError('Please enter a value.')
        return self.cleaned_data['cost']


@view_function
@permission_required('homepage.add_user')
def create(request):

    params = {}

    form = ItemEditForm(initial={
        'name': '',
        'description': '',
        'price': '',
        'owner': '',
        'cost': '',
        'quantityOnHand': '',
        'forSale': '',
    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            itemSpec = hmod.ItemSpecifications()
            itemSpec.name = form.cleaned_data['name']
            itemSpec.description = form.cleaned_data['description']
            itemSpec.user_id = form.cleaned_data['owner']
            itemSpec.price = form.cleaned_data['price']
            item = hmod.Item()
            item.itemSpecifications = itemSpec
            item.cost = form.cleaned_data['cost']
            item.quantityOnHand = form.cleaned_data['quantityOnHand']
            item.forSale = form.cleaned_data['forSale']
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