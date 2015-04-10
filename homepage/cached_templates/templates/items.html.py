# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428636006.671083
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
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
        __M_writer('\r\n\t<h1 class="page-header">Items</h1>\r\n')
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
        __M_writer('\r\n    <a href="#" class="add-item btn btn-success">Add Item</a>\r\n    <table id="items-table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th data-name="itemSpecifications__name">Name</th>\r\n            <th data-name="itemSpecifications__description">Description</th>\r\n            <th data-name="itemSpecifications__price">Price</th>\r\n            <th data-name="itemSpecifications__user__first_name">Owner</th>\r\n            <th data-name="cost">Cost</th>\r\n\t\t\t<th data-name="quantityOnHand">Quantity on Hand</th>\r\n\t\t\t<th data-name="forSale">For Sale</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for item in items:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( item.itemSpecifications.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( item.itemSpecifications.description ))
            __M_writer('</td>\r\n                <td>$')
            __M_writer(str( item.itemSpecifications.price ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( item.itemSpecifications.user.first_name ))
            __M_writer(' ')
            __M_writer(str( item.itemSpecifications.user.last_name ))
            __M_writer('</td>\r\n                <td>$')
            __M_writer(str( item.cost ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( item.quantityOnHand ))
            __M_writer('</td>\r\n')
            if item.forSale == True:
                __M_writer('\t\t\t\t\t<td>Yes</td>\r\n')
            else:
                __M_writer('\t\t\t\t\t<td>No</td>\r\n')
            __M_writer('                <td style="text-align:center;"><a href="#" class="edit-item" data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">Edit</a> | <a href="/homepage/items.delete/')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n\r\n\t<!-- Modal -->\r\n\t<div class="modal fade" id="items-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t    <div class="modal-dialog">\r\n\t\t    <div class="modal-content">\r\n\t\t  \t\t<div class="modal-header">\r\n\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t\t<h4 class="modal-title" id="myModalLabel">Edit</h4>\r\n\t\t  \t\t</div>\r\n\t\t  \t\t<div class="modal-body">\r\n\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/items.html", "line_map": {"64": 7, "71": 7, "72": 20, "73": 21, "74": 22, "75": 22, "76": 23, "77": 23, "78": 24, "79": 24, "80": 25, "81": 25, "82": 25, "83": 25, "84": 26, "85": 26, "86": 27, "87": 27, "88": 28, "89": 29, "90": 30, "27": 0, "92": 33, "93": 33, "94": 33, "95": 33, "96": 33, "97": 36, "91": 31, "37": 1, "103": 97, "42": 5, "52": 3, "58": 3}, "uri": "items.html"}
__M_END_METADATA
"""
