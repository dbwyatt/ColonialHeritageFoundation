# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428686869.056045
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'h1']


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
        def center():
            return render_center(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        def h1():
            return render_h1(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
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


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for item in items:
            __M_writer('\t\t<div class="item-container">\r\n\t\t\t<div class="item" data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('">\r\n\t\t\t\t<div class="photograph" style="background-image:url(\'/static/homepage/media/items/')
            __M_writer(str( item.itemSpecifications.photograph.imagePath ))
            __M_writer('\')"></div>\r\n\t\t\t\t<div class="info">\r\n\t\t\t\t\t<span class="name">')
            __M_writer(str( item.itemSpecifications.name ))
            __M_writer('</span>\r\n')
            if item.forSale != False:
                __M_writer('\t\t\t\t\t\t<span class="price">$')
                __M_writer(str( item.itemSpecifications.price ))
                __M_writer('</span>\r\n')
            __M_writer('\t\t\t\t</div>\r\n\t\t\t\t<div class="purchase">\r\n')
            if item.forSale != False:
                __M_writer('\t\t\t\t\t\t<label class="label">Qty: </label>\r\n\t\t\t\t\t\t<select class=\'quantity\'\r\n')
                if item.quantityOnHand == 0 or item.forSale == False:
                    __M_writer('\t\t\t\t\t\t\t\tdisabled\r\n')
                __M_writer('\t\t\t\t\t\t>\r\n')
                for x in range(item.quantityOnHand):
                    __M_writer('\t\t\t\t\t\t\t\t<option value="')
                    __M_writer(str(x + 1))
                    __M_writer('">')
                    __M_writer(str(x + 1))
                    __M_writer('</option>\r\n')
                __M_writer('\r\n\t\t\t\t\t\t</select>\r\n')
            if item.forSale == False:
                __M_writer('\t\t\t\t\t\t<button class="btn btn-default" disabled>Item not for Sale</button>\r\n')
            elif item.quantityOnHand > 0:
                __M_writer('\t\t\t\t\t\t<button class="buy btn btn-warning" data-id="')
                __M_writer(str( item.entity_ptr_id ))
                __M_writer('">Add to cart</button>\r\n')
            else:
                __M_writer('\t\t\t\t\t\t<button class="btn btn-danger" disabled>Out of stock</button>\r\n')
            __M_writer('\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        __M_writer('\r\n\t<!-- Modal -->\r\n\t<div class="modal fade" id="cart-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t  <div class="modal-dialog">\r\n\t\t<div class="modal-content">\r\n\t\t  <div class="modal-header">\r\n\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t<h4 class="modal-title" id="myModalLabel">Cart</h4>\r\n\t\t  </div>\r\n\t\t  <div class="modal-body">\r\n\t\t\t...\r\n\t\t  </div>\r\n\t\t</div>\r\n\t  </div>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def h1():
            return render_h1(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1 class="page-header">Products</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 11, "65": 11, "66": 12, "67": 12, "68": 14, "69": 14, "70": 15, "71": 16, "72": 16, "73": 16, "74": 18, "75": 20, "76": 21, "77": 23, "78": 24, "79": 26, "80": 27, "81": 28, "82": 28, "83": 28, "84": 28, "85": 28, "86": 30, "87": 33, "88": 34, "89": 35, "90": 36, "27": 0, "92": 36, "93": 37, "94": 38, "95": 40, "96": 44, "91": 36, "102": 3, "38": 1, "43": 5, "108": 3, "114": 108, "53": 7, "61": 7, "62": 9, "63": 10}, "source_encoding": "ascii", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/product.html", "uri": "product.html"}
__M_END_METADATA
"""
