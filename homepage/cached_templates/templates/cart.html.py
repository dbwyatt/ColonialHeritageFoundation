# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428686866.639757
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
        items = context.get('items', UNDEFINED)
        len = context.get('len', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if len(items) > 0:
            __M_writer('\t\t<a href="/homepage/checkout/" class="checkout btn btn-warning">Checkout</a>\r\n')
        else:
            __M_writer('\t\t<p class="empty-cart">Your cart is empty</p>\r\n')
        __M_writer('\r\n\t')
        total_cart = 0 
        
        __M_writer('\r\n\t')
        total = 0 
        
        __M_writer('\r\n\r\n')
        for item in items:
            __M_writer('\t\t<div class="item-container">\r\n\t\t\t<a data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('" class="delete btn btn-danger">Remove</a>\r\n\t\t\t<div class="item" data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">\r\n\t\t\t\t<img class="photograph" src="/static/homepage/media/items/')
            __M_writer(str( item.itemSpecifications.photograph.imagePath ))
            __M_writer('" />\r\n\t\t\t\t<div class="info">\r\n\t\t\t\t\t<span class="name">')
            __M_writer(str( item.itemSpecifications.name ))
            __M_writer('</span><br>\r\n\t\t\t\t\t<span class="price">$')
            __M_writer(str( item.itemSpecifications.price ))
            __M_writer(' item</span><br><br>\r\n\t\t\t\t\t<div class="quantity">\r\n\t\t\t\t\t\t<label for="qty">Qty: </label>\r\n\t\t\t\t\t\t<input name="qty" id="qty" type="text" value=')
            __M_writer(str( item.shopping_cart_quantity))
            __M_writer(' style="width: 50px;display: inline-block;\t"/>\r\n\t\t\t\t\t\t<a data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('" class="update btn btn-warning">Update</a>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<br>\r\n\t\t\t</div>\r\n\r\n\t\t\t')
            total += item.shopping_cart_quantity * item.itemSpecifications.price 
            
            __M_writer('\r\n\t\t\t')
            total_cart += total 
            
            __M_writer('\r\n\t\t\t<div id="total">\r\n\t\t\t\t<span class="item-total-text">Item Total</span><span class="item-total">$')
            __M_writer(str( total ))
            __M_writer('</span>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        __M_writer('\t<div id="total-cart">\r\n\t\t<span class="cart-total-text">Total</span><span class="cart-total">$')
        __M_writer(str( total_cart ))
        __M_writer('</span>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 12, "66": 14, "67": 15, "68": 16, "69": 16, "70": 17, "71": 17, "72": 18, "73": 18, "74": 20, "75": 20, "76": 21, "77": 21, "78": 24, "79": 24, "80": 25, "81": 25, "82": 31, "84": 31, "85": 32, "87": 32, "88": 34, "89": 34, "90": 38, "27": 0, "92": 39, "98": 92, "91": 39, "36": 1, "46": 3, "54": 3, "55": 5, "56": 6, "57": 7, "58": 8, "59": 10, "60": 11, "62": 11, "63": 12}, "source_encoding": "ascii", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/cart.html", "uri": "cart.html"}
__M_END_METADATA
"""
