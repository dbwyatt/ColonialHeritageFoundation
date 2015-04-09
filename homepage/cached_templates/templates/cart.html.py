# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428374099.083224
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/cart.html'
_template_uri = 'cart.html'
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
        len = context.get('len', UNDEFINED)
        items = context.get('items', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for item in items:
            __M_writer('\t\t<div class="item-container">\r\n\t\t\t<div class="item" data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">\r\n\t\t\t\t<div class="photograph" style="background-image:url(\'/static/homepage/media/img/')
            __M_writer(str( item.itemSpecifications.photograph.imagePath ))
            __M_writer('\')"></div>\r\n\t\t\t\t<div class="info">\r\n\t\t\t\t\t<span class="name">')
            __M_writer(str( item.itemSpecifications.name ))
            __M_writer('</span>\r\n\t\t\t\t\t<span class="price">')
            __M_writer(str( item.itemSpecifications.price ))
            __M_writer('</span>\r\n\t\t\t\t</div>\r\n\t\t\t\t<label for="qty">Qty: </label>\r\n\t\t\t\t<input name="qty" id="qty" type="text" value=')
            __M_writer(str( item.shopping_cart_quantity))
            __M_writer(' style="width: 50px;display: inline-block;\t"/>\r\n\t\t\t\t<a data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('" class="update btn btn-warning">Update</a>\r\n\t\t\t\t<a data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('" class="delete btn btn-warning">Delete</a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        __M_writer('\r\n')
        if len(items) > 0:
            __M_writer('\t\t<a href="/homepage/checkout/" class="btn btn-warning">Checkout</a>\r\n')
        else:
            __M_writer('\t\t<p class="empty-cart">Your cart is empty</p>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/cart.html", "source_encoding": "ascii", "uri": "cart.html", "line_map": {"64": 11, "65": 14, "66": 14, "67": 15, "68": 15, "69": 16, "70": 16, "71": 20, "72": 21, "73": 22, "74": 23, "75": 24, "76": 26, "82": 76, "27": 0, "36": 1, "46": 3, "54": 3, "55": 5, "56": 6, "57": 7, "58": 7, "59": 8, "60": 8, "61": 10, "62": 10, "63": 11}}
__M_END_METADATA
"""
