# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428553395.499571
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'h1']


import datetime 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def h1():
            return render_h1(context._locals(__M_locals))
        null = context.get('null', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'h1'):
            context['self'].h1(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def center():
            return render_center(context)
        request = context.get('request', UNDEFINED)
        null = context.get('null', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<address>\r\n\t\t<img class="user-img" src="/static/homepage/media/img/')
        __M_writer(str( user.photograph.imagePath ))
        __M_writer('" /><br><br>\r\n\t\t<strong class="name">Full Name</strong><br>\r\n\t\t<span class="name">')
        __M_writer(str( user.first_name ))
        __M_writer(' ')
        __M_writer(str( user.last_name ))
        __M_writer('</span><br>\r\n\t\t<br>\r\n\t\t<strong>Account Created</strong><br>\r\n\t\t<span class="creation-date">')
        __M_writer(str( datetime.datetime.strftime(user.converted_time, '%A, %B %d, %Y') ))
        __M_writer('<br>')
        __M_writer(str( datetime.datetime.strftime(user.converted_time, '%I:%M %p') ))
        __M_writer('</span>\r\n\t</address>\r\n\t<address>\r\n\t\t<strong>Username</strong><br>\r\n\t\t<span class="username">')
        __M_writer(str( user.username ))
        __M_writer('</span><br>\r\n\t\t<br>\r\n\t\t<strong>Email</strong><br>\r\n\t\t<span class="email">')
        __M_writer(str( user.email ))
        __M_writer('</span><br>\r\n\t\t<br>\r\n\t\t<strong>Phone</strong><br>\r\n\t\t<span class="phone">')
        __M_writer(str( user.phone ))
        __M_writer('</span><br>\r\n\t\t<br>\r\n\t\t<strong>Address</strong><br>\r\n\t\t<span class="address1">')
        __M_writer(str( user.address.address1 ))
        __M_writer('</span><br>\r\n')
        if user.address.address2 is not null:
            __M_writer('\t\t\t<span class="address2">')
            __M_writer(str( user.address.address2 ))
            __M_writer('</span>\r\n')
        __M_writer('\t\t<span class="city-state-zip">')
        __M_writer(str( user.address.city ))
        __M_writer(', ')
        __M_writer(str( user.address.state ))
        __M_writer('  ')
        __M_writer(str( user.address.zip ))
        __M_writer('</span><br>\r\n\t</address>\r\n\t<button class="change-password btn btn-primary" data-id="')
        __M_writer(str( request.session['user_id'] ))
        __M_writer('">Change Password</button>\r\n   \t<button class="update-info btn btn-primary" data-id="')
        __M_writer(str( request.session['user_id'] ))
        __M_writer('">Update Information</button>\r\n\t<!-- Modal -->\r\n\t<div class="modal fade" id="user-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t    <div class="modal-dialog">\r\n\t\t    <div class="modal-content">\r\n\t\t  \t\t<div class="modal-header">\r\n\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t\t<h4 class="modal-title" id="myModalLabel">Edit</h4>\r\n\t\t  \t\t</div>\r\n\t\t  \t\t<div class="modal-body">\r\n\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def h1():
            return render_h1(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1 class="page-header">Account<br><small>View and change your information here</small></h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "account.html", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/account.html", "line_map": {"66": 8, "67": 10, "68": 10, "69": 12, "70": 12, "71": 12, "72": 12, "73": 15, "74": 15, "75": 15, "76": 15, "77": 19, "78": 19, "79": 22, "80": 22, "81": 25, "82": 25, "83": 28, "84": 28, "85": 29, "86": 30, "87": 30, "88": 30, "89": 32, "90": 32, "91": 32, "92": 32, "29": 0, "94": 32, "95": 32, "96": 34, "16": 2, "98": 35, "99": 35, "97": 34, "41": 1, "42": 2, "93": 32, "47": 6, "117": 111, "105": 4, "111": 4, "57": 8}}
__M_END_METADATA
"""
