# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428464562.877548
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        def h1():
            return render_h1(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        total = context.get('total', UNDEFINED)
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
        __M_writer('\r\n\t<h1 class="page-header">Checkout</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t4732817300654<br>\r\n\t411\r\n\t<p>Total Price: $')
        __M_writer(str( total ))
        __M_writer('</p>\r\n\t<form method="POST" action="">\r\n\t\t<table>\r\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t</table>\r\n\t\t<button type="submit" class="btn btn-success">Pay</button>\r\n\t\t<a href="/homepage/checkout.receipt/" class="btn btn-warning">Receipt</a>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.html", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/checkout.html", "line_map": {"65": 7, "27": 0, "38": 1, "73": 7, "74": 10, "75": 10, "76": 13, "77": 13, "43": 5, "83": 77, "53": 3, "59": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
