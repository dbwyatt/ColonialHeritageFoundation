# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423375943.991578
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/areas.html'
_template_uri = 'areas.html'
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
        def center():
            return render_center(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
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
        def center():
            return render_center(context)
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <a href="/homepage/areas.create/" class="btn btn-success">Add Item</a>\r\n    <table id="items-table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th data-name="name">Name</th>\r\n            <th data-name="description">Description</th>\r\n            <th data-name="placeNumber">Place Number</th>\r\n            <th data-name="coordinatingAgentID">Coordinating Agent</th>\r\n            <th data-name="supervisingAgentID">Supervising Agent</th>\r\n            <th data-name="eventID">Event</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for area in areas:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( area.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( area.description ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( area.placeNumber ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( area.coordinatingAgentID.givenName ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( area.supervisingAgentID.givenName ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( area.evenID.name ))
            __M_writer('</td>\r\n                <td style="text-align:center;"><a href="/homepage/areas.edit/')
            __M_writer(str( area.entity_ptr_id ))
            __M_writer('/">Edit</a> | <a href="/homepage/areas.delete/')
            __M_writer(str( area.entity_ptr_id ))
            __M_writer('">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/areas.html", "source_encoding": "ascii", "line_map": {"64": 21, "65": 22, "66": 22, "67": 23, "68": 23, "69": 23, "70": 23, "71": 26, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 15, "54": 16, "55": 17, "56": 17, "57": 18, "58": 18, "59": 19, "60": 19, "61": 20, "62": 20, "63": 21}, "uri": "areas.html"}
__M_END_METADATA
"""
