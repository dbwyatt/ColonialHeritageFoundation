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
import datetime
from django.utils.timezone import localtime

templater = get_renderer('homepage')


@view_function
@login_required
def process_request(request):
    users = {}

    # get user
    try:
        users['user'] = hmod.User.objects.get(id=request.session['user_id'])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/login/')

    users['user'].converted_time = localtime(users['user'].date_joined)

    return templater.render_to_response(request, 'account.html', users)


@view_function
@login_required
def changepassword(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.session['user_id'])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/login/')

    form = ChangePassword(request, initial={
        'old_password': '',
        'password': '',
        'confirm': '',
    })
    if request.method == 'POST':
        form = ChangePassword(request, request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            # form.save()
            update_session_auth_hash(request, user)
            request.session['user_id'] = user.id
            return HttpResponse(True)

    params['form'] = form

    return templater.render_to_response(request, 'account_changepassword.html', params)


class ChangePassword(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        assert isinstance(request, HttpRequest), 'Invalid request object'
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        print(self.request.user.username)
        print(old_password)
        print(password)
        print(confirm)
        user = authenticate(username=self.request.user.username, password=old_password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                if not confirm:
                    # raise forms.ValidationError("You must confirm your password")
                    self.add_error('confirm', 'You must confirm your password')
                elif password != confirm:
                    # raise forms.ValidationError("Passwords do not match")
                    self.add_error('password', 'Passwords do not match')
                    self.add_error('confirm', 'Passwords do not match')
            else:
                self.add_error('old_password', 'The password is valid, but the account has been disabled!')
        else:
            # the authentication system was unable to verify the username and password
            self.add_error('old_password', 'Could not verify password')

        # return confirm


@view_function
def create(request):
    params = {}

    form = UserCreateForm(initial={
        'first_name': '',
        'last_name': '',
        'username': '',
        'password': '',
        'confirm': '',
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
    confirm = forms.CharField(label='Confirm Password', required=False, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Phone')
    securityQuestion = forms.ChoiceField(label='Security Question', choices=[(x, x) for x in ["Where were you born?", "What is your mother's maiden name?", "What is the name of your first pet?", "In which city did you last live?"]])
    securityAnswer = forms.CharField(label='Security Answer')

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Username needs to be at least 5 characters.")
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if not confirm:
            # raise forms.ValidationError("You must confirm your password")
            self.add_error('confirm', 'You must confirm your password')
        elif password != confirm:
            # raise forms.ValidationError("Passwords do not match")
            self.add_error('password', 'Passwords do not match')
            self.add_error('confirm', 'Passwords do not match')

        # return confirm

@view_function
@login_required
def edit(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = UserEditForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'phone': user.phone,
        'address1': user.address.address1,
        'address2': user.address.address2,
        'city': user.address.city,
        'state': user.address.state,
        'zip': user.address.zip,
        'securityQuestion': user.securityQuestion,
        'securityAnswer': user.securityAnswer,
    })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            # try:
            #     address = hmod.Address.objects.get(id=user.address_id)
            # except hmod.User.DoesNotExist:
            #     return HttpResponseRedirect('/homepage/account/')
            address = user.address
            address.address1 = form.cleaned_data['address1']
            address.address2 = form.cleaned_data['address2']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.zip = form.cleaned_data['zip']
            address.save()
            user.securityQuestion = form.cleaned_data['securityQuestion']
            user.securityAnswer = form.cleaned_data['securityAnswer']
            user.save()
            return HttpResponse(True)

    params['form'] = form
    params['user'] = user

    return templater.render_to_response(request, 'account_edit.html', params)


class UserEditForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Phone Number')
    address1 = forms.CharField(label='Address 1')
    address2 = forms.CharField(label='Address 2', required=False)
    city = forms.CharField(label='City')
    state = forms.ChoiceField(
        label='State',
        choices=[
            (x, y) for x, y in
                (
                    ("AL", "Alabama"),
                    ("AK", "Alaska"),
                    ("AS", "American Samoa"),
                    ("AZ", "Arizona"),
                    ("AR", "Arkansas"),
                    ("CA", "California"),
                    ("CO", "Colorado"),
                    ("CT", "Connecticut"),
                    ("DE", "Delaware"),
                    ("DC", "District Of Columbia"),
                    ("FM", "Federated States Of Micronesia"),
                    ("FL", "Florida"),
                    ("GA", "Georgia"),
                    ("GU", "Guam"),
                    ("HI", "Hawaii"),
                    ("ID", "Idaho"),
                    ("IL", "Illinois"),
                    ("IN", "Indiana"),
                    ("IA", "Iowa"),
                    ("KS", "Kansas"),
                    ("KY", "Kentucky"),
                    ("LA", "Louisiana"),
                    ("ME", "Maine"),
                    ("MH", "Marshall Islands"),
                    ("MD", "Maryland"),
                    ("MA", "Massachusetts"),
                    ("MI", "Michigan"),
                    ("MN", "Minnesota"),
                    ("MS", "Mississippi"),
                    ("MO", "Missouri"),
                    ("MT", "Montana"),
                    ("NE", "Nebraska"),
                    ("NV", "Nevada"),
                    ("NH", "New Hampshire"),
                    ("NJ", "New Jersey"),
                    ("NM", "New Mexico"),
                    ("NY", "New York"),
                    ("NC", "North Carolina"),
                    ("ND", "North Dakota"),
                    ("MP", "Northern Mariana Islands"),
                    ("OH", "Ohio"),
                    ("OK", "Oklahoma"),
                    ("OR", "Oregon"),
                    ("PW", "Palau"),
                    ("PA", "Pennsylvania"),
                    ("PR", "Puerto Rico"),
                    ("RI", "Rhode Island"),
                    ("SC", "South Carolina"),
                    ("SD", "South Dakota"),
                    ("TN", "Tennessee"),
                    ("TX", "Texas"),
                    ("UT", "Utah"),
                    ("VT", "Vermont"),
                    ("VI", "Virgin Islands"),
                    ("VA", "Virginia"),
                    ("WA", "Washington"),
                    ("WV", "West Virginia"),
                    ("WI", "Wisconsin"),
                    ("WY", "Wyoming")
                )]
    )
    zip = forms.CharField(label='Zip')
    securityQuestion = forms.ChoiceField(label='Security Question', choices=[(x, x) for x in ["Where were you born?", "What is your mother's maiden name?", "What is the name of your first pet?", "In which city did you last live?"]])
    securityAnswer = forms.CharField(label='Security Answer')

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Username needs to be at least 5 character.")
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']


@view_function
@login_required
def recent_activity(request):
    users = {}

    # get user
    try:
        users['user'] = hmod.User.objects.get(id=request.session['user_id'])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/')

    users['user'].converted_time = localtime(users['user'].last_login)

    return templater.render_to_response(request, 'account_recent_activity.html', users)