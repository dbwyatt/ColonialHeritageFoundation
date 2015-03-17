__author__ = 'Daniel'

from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.models import User, Group, Permission, ContentType
from django.contrib.auth.decorators import permission_required, login_required

templater = get_renderer('homepage')


@view_function
@permission_required('homepage.admin')
def process_request(request):
    users = {}
    users['users'] = hmod.User.objects.all().order_by('last_name')

    return templater.render_to_response(request, 'users.html', users)


@view_function
@permission_required('homepage.admin')
def edit(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    try:
        group = Group.objects.get(name=user.groups.all()[0])
    except Exception as e:
        group = 3

    form = UserEditForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'securityQuestion': user.securityQuestion,
        'securityAnswer': user.securityAnswer,
        'group': group.id if group is not 3 else group
    })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.securityQuestion = form.cleaned_data['securityQuestion']
            user.securityAnswer = form.cleaned_data['securityAnswer']

            user.groups.clear()
            user.groups.add(form.cleaned_data['group'])

            user.save()
            return HttpResponse(True)

    params['form'] = form
    params['user'] = user

    return templater.render_to_response(request, 'users_edit.html', params)


class UserEditForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email', required=True)
    securityQuestion = forms.ChoiceField(label='Security Question', choices=[(x, x) for x in ["Where were you born?", "What is your mother's maiden name?", "What is the name of your first pet?", "In which city did you last live?"]])
    securityAnswer = forms.CharField(label='Security Answer')
    group = forms.ChoiceField(label='Group', choices=[(x.id, x.name) for x in Group.objects.all()])

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Username needs to be at least 5 character.")
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']


@view_function
def changepassword(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = ChangePassword(initial={
        'password': user.password
    })
    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/homepage/users/')

    params['form'] = form

    return templater.render_to_response(request, 'users_changepassword.html', params)


class ChangePassword(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


@view_function
@permission_required('homepage.create_user')
def create(request):

    params = {}

    form = UserCreateForm(initial={
        'first_name': '',
        'last_name': '',
        'username': '',
        'password': '',
        'email': '',
        'securityQuestion': '',
        'securityAnswer': '',
        'group': 3
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
            user.securityQuestion = form.cleaned_data['securityQuestion']
            user.securityAnswer = form.cleaned_data['securityAnswer']
            user.save()
            return HttpResponseRedirect('/homepage/users/')

    params['form'] = form

    return templater.render_to_response(request, 'users_edit.html', params)


class UserCreateForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)
    securityQuestion = forms.ChoiceField(label='Security Question', choices=[(x, x) for x in ["Where were you born?", "What is your mother's maiden name?", "What is the name of your first pet?", "In which city did you last live?"]])
    securityAnswer = forms.CharField(label='Security Answer')
    group = forms.ChoiceField(label='Group', choices=[(x.id, x.name) for x in Group.objects.all()])

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Username needs to be at least 5 character.")
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']

@view_function
def delete(request):
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    user.delete()
    return HttpResponseRedirect('/homepage/users/')


@view_function
def order(request):
    users = {}
    users['users'] = hmod.User.objects.all().order_by(request.urlparams[0])

    return templater.render_to_response(request, 'users.html', users)