__author__ = 'Daniel'

from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, Group, Permission, ContentType
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login

templater = get_renderer('homepage')


@view_function
@login_required
def process_request(request):
    users = {}

    # get user
    try:
        users['users'] = hmod.User.objects.get(id=request.session['user_id'])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/login/')

    return templater.render_to_response(request, 'account.html', users)


@view_function
@login_required
def changepassword(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.session['user_id'])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/login/')

    form = ChangePassword(initial={
        'password': user.password
    })
    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            # form.save()
            update_session_auth_hash(request, user)
            request.session['user_id'] = user.id
            return HttpResponse(True)

    params['form'] = form

    return templater.render_to_response(request, 'users_changepassword.html', params)


class ChangePassword(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


@view_function
def create(request):
    params = {}

    form = UserCreateForm(initial={
        'first_name': '',
        'last_name': '',
        'username': '',
        'password': '',
        'email': '',
        'phone': '',
        'securityQuestion': '',
        'securityAnswer': ''
    })
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        form.userid = -1
        if form.is_valid():
            user = hmod.User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.address = hmod.Address.objects.all()[0]
            user.phone = form.cleaned_data['phone']
            user.securityQuestion = form.cleaned_data['securityQuestion']
            user.securityAnswer = form.cleaned_data['securityAnswer']
            user.photograph = hmod.Photograph.objects.all()[0]
            group = Group.objects.get(name='User')
            user.group = group
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            request.session['user_id'] = user.id
            return HttpResponseRedirect('/homepage/account/')

    params['form'] = form

    return templater.render_to_response(request, 'account_create.html', params)


class UserCreateForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Phone')
    securityQuestion = forms.ChoiceField(label='Security Question', choices=[(x, x) for x in ["Where were you born?", "What is your mother's maiden name?", "What is the name of your first pet?", "In which city did you last live?"]])
    securityAnswer = forms.CharField(label='Security Answer')

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Username needs to be at least 5 character.")
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']