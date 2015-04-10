# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428641327.322671
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/product.html'
_template_uri = 'product.html'
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "product.html", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/product.html", "line_map": {"65": 7, "107": 40, "73": 7, "74": 9, "75": 10, "76": 11, "77": 11, "78": 12, "79": 12, "80": 14, "81": 14, "82": 15, "83": 16, "84": 16, "85": 16, "86": 18, "87": 20, "88": 21, "89": 23, "90": 24, "27": 0, "92": 27, "93": 28, "94": 28, "95": 28, "96": 28, "97": 28, "98": 30, "91": 26, "100": 34, "101": 35, "38": 1, "103": 36, "104": 36, "105": 37, "106": 38, "43": 5, "108": 44, "99": 33, "114": 108, "53": 3, "59": 3, "102": 36}}
__M_END_METADATA
"""
