# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423376988.673188
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/venues_edit.html'
_template_uri = 'venues_edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center']


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
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

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
        __M_writer('\r\n    <form method="POST">\r\n        <table>\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n        </table>\r\n        <a href="/homepage/venues/" class="btn btn-warning">Cancel</a>\r\n        <button type="submit" class="btn btn-primary">Save</button>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/venues_edit.html", "line_map": {"35": 1, "52": 3, "53": 6, "54": 6, "27": 0, "60": 54, "45": 3}, "source_encoding": "ascii", "uri": "venues_edit.html"}
__M_END_METADATA
"""
