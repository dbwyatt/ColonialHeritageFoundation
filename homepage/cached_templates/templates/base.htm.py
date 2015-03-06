# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425618781.37164
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'footer', 'header', 'left', 'title']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n\t<title>\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\t</title>\r\n\r\n')
        __M_writer('\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/jquery.form.js"></script>\r\n\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\r\n\t<link rel="icon" type="image/x-icon" href="/static/homepage/media/featehr.png" />\r\n\r\n')
        __M_writer('\t')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body >\r\n\r\n\t<div id="header">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n\r\n\t<div id="left" class="col-md-1">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n\r\n\t<div id="center" class="col-md-10">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n\r\n\t<div id="footer">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n\r\n\r\n')
        __M_writer('\t')
        __M_writer(str( static_renderer.get_template_js(request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t<nav class="navbar navbar-default">\r\n\t\t\t  <div class="container-fluid">\r\n\t\t\t\t<!-- Brand and toggle get grouped for better mobile display -->\r\n\t\t\t\t<div class="navbar-header">\r\n\t\t\t\t  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n\t\t\t\t\t<span class="sr-only">Toggle navigation</span>\r\n\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t  </button>\r\n\t\t\t\t  <a class="navbar-brand" href="/homepage">\r\n\t\t\t\t\t  <div class="image">\r\n\t\t\t\t\t\t<img src="/static/homepage/media/headerimg.png">\r\n\t\t\t\t\t  </div>\r\n\t\t\t\t\t  <span>Colonial Heritage Foundation</span>\r\n\t\t\t\t  </a>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<!-- Collect the nav links, forms, and other content for toggling -->\r\n\t\t\t\t<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n\t\t\t\t  <ul class="nav navbar-nav navbar-left">\r\n')
        if user.is_authenticated():
            __M_writer('\t\t\t\t\t<li class="dropdown">\r\n\t\t\t\t\t  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Admin<span class="caret"></span></a>\r\n\t\t\t\t\t  <ul class="dropdown-menu" role="menu">\r\n\t\t\t\t\t\t<li><a href="/homepage/areas/">Areas</a></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/events/">Events</a></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/venues/">Venues</a></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/items/">Items</a></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/rentableitems/">Rentable Items</a></li>\r\n\t\t\t\t\t\t<li class="divider"></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/users/">Users</a></li>\r\n\t\t\t\t\t\t<li><a href="#">Agents: New/Edit</a></li>\r\n\t\t\t\t\t  </ul>\r\n\t\t\t\t\t</li>\r\n')
        __M_writer('\t\t\t\t  </ul>\r\n\r\n\t\t\t\t  <ul class="nav navbar-nav navbar-right">\r\n')
        if user.is_authenticated():
            __M_writer('\t\t\t\t\t  <li class="dropdown">\r\n\t\t\t\t\t\t<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Account<span class="caret"></span></a>\r\n\t\t\t\t\t\t<ul class="dropdown-menu" role="menu">\r\n\t\t\t\t\t\t  <li><a href="#">Summary</a></li>\r\n\t\t\t\t\t\t  <li><a href="#">Recent Activity</a></li>\r\n\t\t\t\t\t\t  <li><a href="#">Something else here</a></li>\r\n\t\t\t\t\t\t <li class="divider"></li>\r\n\t\t\t\t\t\t  <li><a href="#">Account Details</a></li>\r\n\t\t\t\t\t\t  <li class="divider"></li>\r\n\t\t\t\t\t\t  <li><a href="/homepage/logout/">Log Out</a></li>\r\n\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t  </li>\r\n\t\t\t\t\t  <li><a href="/homepage/logout/">Logout</a></li>\r\n')
        else:
            __M_writer('\t\t\t\t\t  <li>\r\n\t\t\t\t\t\t  <a id="login-button" data-toggle="modal" data-target="#login-modal" type="button">Login</a>\r\n\t\t\t\t\t\t  <!-- <ul class="dropdown-menu login-form" role="menu">\r\n\t\t\t\t\t\t\t<div id="login-container">\r\n\t\t\t\t\t\t\t  <form id="login-form" method="POST" action="/homepage/login/">\r\n\t\t\t\t\t\t\t\t<label for="username"><span class="label label-primary">Username</span></label>\r\n\t\t\t\t\t\t\t\t<input id="username" name=username type="text" />\r\n\t\t\t\t\t\t\t\t<label for="password"><span class="label label-primary">Password</span></label>\r\n\t\t\t\t\t\t\t\t<input id="password" name=password type="password" />\r\n\t\t\t\t\t\t\t\t<button id="login" type="submit">Login</button>\r\n\t\t\t\t\t\t\t  </form>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t  </ul> -->\r\n\t\t\t\t\t  </li>\r\n')
        __M_writer('\t\t\t\t  </ul>\r\n\t\t\t\t</div><!-- /.navbar-collapse -->\r\n\t\t\t  </div><!-- /.container-fluid -->\r\n\t\t\t</nav>\r\n\r\n\t\t\t<!-- Modal -->\r\n\t\t\t<div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t\t\t  <div class="modal-dialog">\r\n\t\t\t\t<div class="modal-content">\r\n\t\t\t\t  <div class="modal-header">\r\n\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t\t<h4 class="modal-title" id="myModalLabel">Login</h4>\r\n\t\t\t\t  </div>\r\n\t\t\t\t  <div class="modal-body">\r\n\t\t\t\t\t...\r\n\t\t\t\t  </div>\r\n\t\t\t\t</div>\r\n\t\t\t  </div>\r\n\t\t\t</div>\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\tColonial Heritage Foundation\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 128, "128": 127, "107": 34, "69": 133, "134": 127, "140": 13, "74": 138, "75": 143, "76": 143, "77": 143, "16": 4, "115": 56, "18": 0, "83": 132, "121": 89, "152": 146, "89": 132, "101": 137, "118": 74, "95": 137, "37": 2, "38": 4, "39": 5, "43": 5, "114": 34, "48": 15, "49": 19, "50": 21, "51": 21, "52": 28, "53": 28, "54": 28, "119": 75, "120": 88, "116": 57, "122": 104, "59": 123, "146": 13, "117": 71}, "source_encoding": "ascii", "uri": "base.htm", "filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/base.htm"}
__M_END_METADATA
"""
