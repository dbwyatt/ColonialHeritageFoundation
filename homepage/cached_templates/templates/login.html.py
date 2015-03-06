# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425538144.365466
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form id="login-form" method="POST" action="/homepage/index.loginform/">\r\n\t\t<table>\r\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t</table>\r\n\t\t<button type="submit" class="btn btn-primary">Login</button>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/login.html", "line_map": {"35": 1, "52": 3, "53": 6, "54": 6, "27": 0, "60": 54, "45": 3}, "source_encoding": "ascii", "uri": "login.html"}
__M_END_METADATA
"""
