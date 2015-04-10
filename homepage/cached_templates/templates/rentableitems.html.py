# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428687054.309204
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/rentableitems.html'
_template_uri = 'rentableitems.html'
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
        def center():
            return render_center(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
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
        __M_writer('\r\n\t<h1 class="page-header">Rentable Items</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <a href="/homepage/rentableitems.create/" class="btn btn-success pull-right" style="margin-bottom: 20px;">Add Rental Item</a>\r\n    <table id="items-table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th data-name="name">Name</th>\r\n            <th data-name="description">Description</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for item in items:
            __M_writer('            <tr data-id="')
            __M_writer(str( item.wardrobeitem_ptr_id ))
            __M_writer('">\r\n                <td>')
            __M_writer(str( item.wardrobeitem_ptr.serializeditem_ptr.item_ptr.itemSpecifications.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( item.dailyPrice ))
            __M_writer('</td>\r\n                <td style="text-align:center;"><a href="/homepage/rentableitems.edit/')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('/">Edit</a> | <a href="/homepage/rentableitems.delete/')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "rentableitems.html", "line_map": {"64": 7, "90": 84, "37": 1, "71": 7, "72": 15, "73": 16, "74": 16, "75": 16, "76": 17, "77": 17, "78": 18, "79": 18, "80": 19, "81": 19, "82": 19, "83": 19, "52": 3, "84": 22, "58": 3, "27": 0, "42": 5}, "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/rentableitems.html"}
__M_END_METADATA
"""
