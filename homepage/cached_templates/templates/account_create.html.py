# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428687111.355568
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/account_create.html'
_template_uri = 'account_create.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['h1', 'center']


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
        form = context.get('form', UNDEFINED)
        def h1():
            return render_h1(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'h1'):
            context['self'].h1(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def h1():
            return render_h1(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1 class="page-header">Register<br><small>Fill out all fields to create an account</small></h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form id="new-user-form" method="POST" action="/homepage/account.create/">\r\n\t\t<table>\r\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t</table>\r\n\t\t<button type="submit" class="btn btn-warning">Create</button>\r\n\t\t<a href="/homepage/" type="button" class="btn btn-default">Cancel</a>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "account_create.html", "line_map": {"64": 7, "52": 3, "37": 1, "71": 7, "72": 10, "73": 10, "58": 3, "27": 0, "42": 5, "79": 73}, "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/account_create.html"}
__M_END_METADATA
"""
