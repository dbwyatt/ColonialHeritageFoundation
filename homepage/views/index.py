__author__ = 'Daniel'

from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}
    return templater.render_to_response(request, 'index.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # checking for ldap credentials
        auth = False
        localdomain = "@colonialfoundations.local"
        ldapUsername = str(username) + localdomain
        try:
            s = Server('www.colonialfoundations.com', port=3899, get_info=GET_ALL_INFO)
            c = Connection(
                s,
                auto_bind=True,
                client_strategy=STRATEGY_SYNC,
                user=ldapUsername,
                password='212BrickOven',
                authentication=AUTH_SIMPLE,
                raise_exceptions=False
            )
            if c.response:
                print("Bad user info")
            else:
                auth = True

        except Exception:
            print("Bad user credentials {} {}".format(ldapUsername, password))

        if auth:
            user = None
            try:
                user = hmod.User.objects.get(username=username)
            except hmod.User.DoesNotExist:
                print("Does not exist")

            if user:
                print("saving previous user")
                user.set_password(password)
                user.save()
            elif user is None and username is not None:
                user = hmod.User()
                user.first_name = ''
                user.last_name = ''
                user.username = username
                user.set_password(password)
                user.email = username + "@colonialfoundations.com"
                user.photograph_id = 1
                user.address_id = 2
                user.is_superuser = True
                user.requiresReset = False

                print("saving new user")
                user.save()
            else:
                print("none")
        else:
            print("no ldap")

        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None and username is not None and password is not None:
            raise forms.ValidationError('No user was found for these credentials. Please re-enter information.')
        return self.cleaned_data


@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            user = hmod.User.objects.get(username=form.cleaned_data['username'])
            request.session['user_id'] = user.id
            try:
                del request.session['need_to_login']
            except KeyError:
                pass
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            params['logged_in'] = True
            return HttpResponse(params)

    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)


@view_function
def logout_page(request):
    logout(request)

    return HttpResponse("Logout")


@view_function
def search(request):
    search = {}
    item_spec = hmod.ItemSpecifications.objects.filter(name__icontains=request.urlparams[0])
    search['items'] = hmod.Item.objects.filter(itemSpecifications__in=item_spec)

    search['event'] = hmod.Event.objects.filter(name__icontains=request.urlparams[0])

    print(search['event'])

    return templater.render_to_response(request, 'product.html', search)
