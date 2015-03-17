# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425794702.025887
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/product.html'
_template_uri = 'product.html'
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
            __M_writer('</span>\r\n\t\t\t\t</div>\r\n\t\t\t\t<button class="buy btn btn-warning" data-id="')
            __M_writer(str( item.entity_ptr_id ))
            __M_writer('" data-target="#cart-modal" data-toggle="modal">Buy</button>\r\n\t\t\t\t<select class=\'quantity\'>\r\n\t\t\t\t\t<option value=\'1\'>1</option>\r\n\t\t\t\t\t<option value=\'2\'>2</option>\r\n\t\t\t\t\t<option value=\'3\'>3</option>\r\n\t\t\t\t\t<option value=\'4\'>4</option>\r\n\t\t\t\t\t<option value=\'5\'>5</option>\r\n\t\t\t\t\t<option value=\'6\'>6</option>\r\n\t\t\t\t\t<option value=\'7\'>7</option>\r\n\t\t\t\t\t<option value=\'8\'>8</option>\r\n\t\t\t\t\t<option value=\'9\'>9</option>\r\n\t\t\t\t\t<option value=\'10\'>10</option>\r\n\t\t\t\t</select>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        __M_writer('\r\n\t<!-- Modal -->\r\n\t\t<div class="modal fade" id="cart-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t\t  <div class="modal-dialog">\r\n\t\t\t<div class="modal-content">\r\n\t\t\t  <div class="modal-header">\r\n\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t<h4 class="modal-title" id="myModalLabel">Cart</h4>\r\n\t\t\t  </div>\r\n\t\t\t  <div class="modal-body">\r\n\t\t\t\t...\r\n\t\t\t  </div>\r\n\t\t\t</div>\r\n\t\t  </div>\r\n\t\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/product.html", "line_map": {"64": 13, "65": 29, "35": 1, "71": 65, "45": 3, "27": 0, "52": 3, "53": 5, "54": 6, "55": 7, "56": 7, "57": 8, "58": 8, "59": 10, "60": 10, "61": 11, "62": 11, "63": 13}, "uri": "product.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
