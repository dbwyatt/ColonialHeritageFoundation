# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423368971.808534
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <a href="/homepage/items.create/" class="btn btn-success">Add Item</a>\r\n    <table id="items-table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th data-name="name">Name</th>\r\n            <th data-name="description">Description</th>\r\n            <th data-name="value">Value</th>\r\n            <th data-name="standardRentalPrice">Rental Price</th>\r\n            <th data-name="owner">Owner</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for item in items:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( item.description ))
            __M_writer('</td>\r\n                <td>$ ')
            __M_writer(str( item.value ))
            __M_writer('</td>\r\n                <td>$ ')
            __M_writer(str( item.standardRentalPrice ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( item.legalEntityID.givenName ))
            __M_writer('</td>\r\n                <td style="text-align:center;"><a href="/homepage/items.edit/')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('/">Edit</a> | <a href="/homepage/items.delete/')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 20, "65": 21, "66": 21, "67": 21, "68": 21, "69": 24, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 14, "54": 15, "55": 16, "56": 16, "57": 17, "58": 17, "59": 18, "60": 18, "61": 19, "62": 19, "63": 20}, "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/items.html", "uri": "items.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
