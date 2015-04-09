# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428618840.468767
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        __M_writer('\r\n\t<h1 class="page-header">Events</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <a href="/homepage/events.create/" class="btn btn-success">Add Event</a>\r\n    <table id="items-table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th data-name="name">Name</th>\r\n            <th data-name="description">Description</th>\r\n            <th data-name="startDate">Start Date</th>\r\n            <th data-name="endDate">End Date</th>\r\n            <th data-name="mapFileName">Map File</th>\r\n            <th data-name="venueID">Venue</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for event in events:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( event.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( event.description ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( event.startDate ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( event.endDate ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( event.mapFileName ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( event.venueName ))
            __M_writer('</td>\r\n                <td style="text-align:center;"><a href="/homepage/events.edit/')
            __M_writer(str( event.entity_ptr_id ))
            __M_writer('/">Edit</a> | <a href="/homepage/events.delete/')
            __M_writer(str( event.entity_ptr_id ))
            __M_writer('">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/events.html", "uri": "events.html", "line_map": {"64": 7, "71": 7, "72": 19, "73": 20, "74": 21, "75": 21, "76": 22, "77": 22, "78": 23, "79": 23, "80": 24, "81": 24, "82": 25, "83": 25, "84": 26, "85": 26, "86": 27, "87": 27, "88": 27, "89": 27, "90": 30, "27": 0, "96": 90, "37": 1, "42": 5, "52": 3, "58": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
