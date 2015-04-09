# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428618514.304003
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        __M_writer('\r\n\t<h1 class="page-header">Users</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<a href="#" class="add-user btn btn-success">Add User</a>\r\n    <table id="users-table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th data-name="first_name">First Name</th>\r\n            <th data-name="last_name">Last Name</th>\r\n            <th data-name="username">Username</th>\r\n            <th data-name="email">Email</th>\r\n            <th id="change-password">Password</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for user in users:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.username ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\r\n                <td><a href="#" class="change-password" data-id="')
            __M_writer(str( user.id ))
            __M_writer('">Change Password</a></td>\r\n                <td style="text-align:center;"><a href="#" class="edit-user" data-id="')
            __M_writer(str( user.id ))
            __M_writer('">Edit</a> | <a href="/homepage/users.delete/')
            __M_writer(str( user.id ))
            __M_writer('/" class="delete-user">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n\r\n\t<!-- Modal -->\r\n\t<div class="modal fade" id="user-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t    <div class="modal-dialog">\r\n\t\t    <div class="modal-content">\r\n\t\t  \t\t<div class="modal-header">\r\n\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t\t<h4 class="modal-title" id="myModalLabel">Edit</h4>\r\n\t\t  \t\t</div>\r\n\t\t  \t\t<div class="modal-body">\r\n\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/users.html", "uri": "users.html", "line_map": {"64": 7, "71": 7, "72": 18, "73": 19, "74": 20, "75": 20, "76": 21, "77": 21, "78": 22, "79": 22, "80": 23, "81": 23, "82": 24, "83": 24, "84": 25, "85": 25, "86": 25, "87": 25, "88": 28, "27": 0, "94": 88, "37": 1, "42": 5, "52": 3, "58": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
