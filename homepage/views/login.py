__author__ = 'Daniel'

from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login

templater = get_renderer('homepage')


@view_function
def process_request(request):
    request.session['need_to_login'] = True
    return HttpResponseRedirect('/homepage/')
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/homepage/users/')

    params['form'] = form

    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None and username is not None and password is not None:
            raise forms.ValidationError('No user was found for these credentials. Please re-enter information.')
        return self.cleaned_data