__author__ = 'Daniel'


from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, logout

templater = get_renderer('homepage')


@view_function
def process_request(request):
    logout(request)

    return HttpResponseRedirect('/homepage/')