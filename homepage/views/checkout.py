from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required, login_required
import requests
import datetime
from django.core.mail import send_mail


templater = get_renderer('homepage')


@view_function
@login_required
def process_request(request):
    params = {}

    total = 0
    for x in hmod.Item.objects.filter(entity_ptr_id__in=request.session['shopping_cart'].keys()):
        total += x.itemSpecifications.price * request.session['shopping_cart'][str(x.entity_ptr_id)]
    params['total'] = total

    form = PaymentForm(initial={
        'type': 'Visa',
        'number': '4732817300654',
        'exp_month': '10',
        'exp_year': '2015',
        'cvc': '411',
        'name': 'Cosmo Limesandal',
    })
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '9130650c7be1e217e548fd3cd6858379'

            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': total,
                'type': form.cleaned_data['type'],
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
                'name': form.cleaned_data['name'],
                'description': 'Charge for cosmo@is411.byu.edu'
            })

            print(r.text)

            resp = r.json()
            if 'error' in resp:
                print("ERROR", resp['error'])
                params['error'] = "There was an error with your transaction. {}. Please try again.".format(resp['error'])
                return templater.render_to_response(request, 'checkout.error.html', params)
            else:
                print(resp.keys())
                print(resp['ID'])
                params['success'] = "Thank you! Transaction Complete! A message has been sent to your email with purchase details. Your items will be sent to you soon."

                email = {}
                if 'shopping_cart' not in request.session:
                    request.session['shopping_cart'] = {}

                email['items'] = hmod.Item.objects.filter(entity_ptr_id__in=request.session['shopping_cart'].keys())
                email['cart'] = request.session['shopping_cart']
                email['total'] = total

                for x in email['items']:
                    x.shopping_cart_quantity = email['cart'][str(x.entity_ptr_id)]

                emailsubject = "Colonial Heritage Foundation Purchase"
                to_email = hmod.User.objects.get(id=request.user.id)
                from_email = settings.EMAIL_HOST_USER
                emailbody = templater.render(request, 'checkout_receipt.html', email)
                send_mail(emailsubject, emailbody, from_email, [to_email.email], html_message=emailbody, fail_silently=False)

                del request.session['shopping_cart']
                return templater.render_to_response(request, 'checkout.success.html', params)

    params['form'] = form

    return templater.render_to_response(request, 'checkout.html', params)


class PaymentForm(forms.Form):
    type = forms.ChoiceField(choices=[(x, x) for x in ['Visa']])
    number = forms.CharField()
    exp_month = forms.ChoiceField(choices=[(x, x) for x in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']])
    exp_year = forms.ChoiceField(choices=[(x, x) for x in [15, 16, 17, 18, 19]])
    cvc = forms.CharField()
    name = forms.CharField()


@view_function
def receipt(request):
    params = {}

    return templater.render_to_response(request, 'receipt.html', params)