# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428654079.787418
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'footer', 'title', 'jumbotron', 'h1', 'center', 'header']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def h1():
            return render_h1(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <meta name="description" content="Management system for the Colonial Heritage Foundation.">\r\n  <meta name="keywords" content="CHF, Colonial Heritage Foundation">\r\n  <head>\r\n\r\n\t<title>\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\t</title>\r\n\r\n')
        __M_writer('\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/jquery.form.js"></script>\r\n\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\r\n\t<link rel="icon" type="image/x-icon" href="/static/homepage/media/feather.png" />\r\n\r\n')
        __M_writer('\t')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body >\r\n\r\n\t<div id="header">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n\r\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n\t<div id="left" class="col-md-1">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n\r\n\t<div id="center" class="col-md-12">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'h1'):
            context['self'].h1(**pageargs)
        

        __M_writer('\r\n\t\t')
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


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t<ul>\r\n\t\t\t\t<li class="footer-list">\r\n\t\t\t\t\t<span class="footer-item-header footer-item">Company</span>\r\n\t\t\t\t\t<a class="footer-item">About Us</a>\r\n\t\t\t\t\t<a class="footer-item">Contact Us</a>\r\n\t\t\t\t</li>\r\n\t\t\t</ul>\r\n\t\t\t<span class="copyright pull-right">Copyright &copy; Colonial Heritage Foundation, Inc.</span>\r\n\t\t')
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


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def h1():
            return render_h1(context)
        __M_writer = context.writer()
        __M_writer('<h1 class="page-header">Colonial Heritage Foundation</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer("\r\n\t\t\t<p>\r\n\t\t\t\tWe are the Colonial Heritage Foundation. We seek to create a fun learning environment in which individuals can learn more about our country's heritage while have fun at the same time.\r\n\t\t\t</p>\r\n\t\t")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def header():
            return render_header(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t<nav class="navbar navbar-default">\r\n\t\t\t  <div class="container-fluid">\r\n\t\t\t\t<!-- Brand and toggle get grouped for better mobile display -->\r\n\t\t\t\t<div class="navbar-header">\r\n\t\t\t\t  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n\t\t\t\t\t<span class="sr-only">Toggle navigation</span>\r\n\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t  </button>\r\n\t\t\t\t  <a class="navbar-brand" href="/homepage">\r\n\t\t\t\t\t  <div class="image">\r\n\t\t\t\t\t\t<img src="/static/homepage/media/headerimg.png">\r\n\t\t\t\t\t  </div>\r\n\t\t\t\t\t  <span>Colonial Heritage Foundation</span>\r\n\t\t\t\t  </a>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<!-- Collect the nav links, forms, and other content for toggling -->\r\n\t\t\t\t<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n\t\t\t\t  <ul class="nav navbar-nav navbar-left">\r\n\t\t\t\t\t<li><a href="/homepage/product/">Product</a></li>\r\n\t\t\t\t\t<li><a href="/homepage/view_events/">Events</a></li>\r\n')
        if user.is_authenticated() and user.is_superuser:
            __M_writer('\t\t\t\t\t<li class="dropdown">\r\n\t\t\t\t\t  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Admin<span class="caret"></span></a>\r\n\t\t\t\t\t  <ul class="dropdown-menu" role="menu">\r\n\t\t\t\t\t    <li><a href="/homepage/items/">Items</a></li>\r\n\t\t\t\t\t    <li><a href="/homepage/events/">Events</a></li>\r\n\t\t\t\t\t\t  <li><a href="/homepage/rentableitems/">Rentable Items</a></li>\r\n\t\t\t\t\t\t  <li><a href="/homepage/users/">Users</a></li>\r\n\t\t\t\t\t\t  <li class="divider"></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/rentableitems.late/">Late Rentals</a></li>\r\n\t\t\t\t\t\t<li><a href="/homepage/rentableitems_return/">Returns</a></li>\r\n\t\t\t\t\t  </ul>\r\n\t\t\t\t\t</li>\r\n')
        __M_writer('\t\t\t\t  </ul>\r\n\r\n\t\t\t\t  <ul class="nav navbar-nav navbar-right">\r\n')
        if user.is_authenticated():
            __M_writer('\t\t\t\t\t  <li>\r\n\t\t\t\t\t\t  <a class="cart" data-target="#cart-modal" data-toggle="modal">Cart\r\n\t\t\t\t\t\t\t  <img src="/static/homepage/media/cart.png" />\r\n\t\t\t\t\t\t\t  <sup>\r\n\t\t\t\t\t\t\t\t  <div class="badge">\r\n\t\t\t\t\t\t\t\t\t  ')
            cart_length = 0 
            
            __M_writer('\r\n')
            if 'shopping_cart' in request.session:
                for x, y in request.session['shopping_cart'].items():
                    __M_writer('\t\t\t\t\t\t\t\t\t\t\t  ')
                    cart_length += int(y) 
                    
                    __M_writer('\r\n')
            __M_writer('\t\t\t\t\t\t\t\t\t  ')
            __M_writer(str( cart_length ))
            __M_writer('\r\n\t\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t  </sup>\r\n\t\t\t\t\t\t  </a>\r\n\t\t\t\t\t  </li>\r\n\t\t\t\t\t  <li class="dropdown">\r\n\t\t\t\t\t\t<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Your Account<span class="caret"></span></a>\r\n\t\t\t\t\t\t<ul class="dropdown-menu" role="menu">\r\n\t\t\t\t\t\t  <li><p><strong>Hello, ')
            __M_writer(str( user.first_name ))
            __M_writer('</strong></p></li>\r\n\t\t\t\t\t\t  <li class="divider"></li>\r\n\t\t\t\t\t\t  <li><a href="/homepage/account.recent_activity/">Recent Activity</a></li>\r\n\t\t\t\t\t\t  <li><a href="/homepage/account/">Account Details</a></li>\r\n\t\t\t\t\t\t  <li class="divider"></li>\r\n\t\t\t\t\t\t  <li><a href="#" id="logout-button">Log Out</a></li>\r\n\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t  </li>\r\n\t\t\t\t\t  <!-- <li><a id="logout-button">Logout</a></li> -->\r\n')
        else:
            __M_writer('\t\t\t\t\t  <li>\r\n\t\t\t\t\t\t  <a id="login-button" data-toggle="modal" data-target="#login-modal" type="button">Login</a>\r\n\t\t\t\t\t\t  <!-- <ul class="dropdown-menu login-form" role="menu">\r\n\t\t\t\t\t\t\t<div id="login-container">\r\n\t\t\t\t\t\t\t  <form id="login-form" method="POST" action="/homepage/login/">\r\n\t\t\t\t\t\t\t\t<label for="username"><span class="label label-primary">Username</span></label>\r\n\t\t\t\t\t\t\t\t<input id="username" name=username type="text" />\r\n\t\t\t\t\t\t\t\t<label for="password"><span class="label label-primary">Password</span></label>\r\n\t\t\t\t\t\t\t\t<input id="password" name=password type="password" />\r\n\t\t\t\t\t\t\t\t<button id="login" type="submit">Login</button>\r\n\t\t\t\t\t\t\t  </form>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t  </ul> -->\r\n\t\t\t\t\t  </li>\r\n\t\t\t\t\t  <li><a href="/homepage/account.create/">Register</a></li>\r\n')
        __M_writer('\t\t\t\t  </ul>\r\n\t\t\t\t</div><!-- /.navbar-collapse -->\r\n\t\t\t  </div><!-- /.container-fluid -->\r\n\t\t\t</nav>\r\n\r\n\t\t\t<!-- Search Bar -->\r\n\t\t\t<div id="search">\r\n\t\t\t\t<div id="search-container">\r\n\t\t\t\t\t<form id="search-form" method="POST">\r\n\t\t\t\t\t\t<img src="/static/homepage/media/search.png" />\r\n\t\t\t\t\t\t<input type="text" id="search-box" />\r\n\t\t\t\t\t\t<button type="button" for="search-box" id="search-button">Search</button>\r\n\t\t\t\t\t</form>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\r\n\t\t\t<!-- Modal -->\r\n\t\t\t<div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t\t\t  <div class="modal-dialog">\r\n\t\t\t\t<div class="modal-content">\r\n\t\t\t\t  <div class="modal-header">\r\n\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t\t<h4 class="modal-title" id="myModalLabel">Login</h4>\r\n\t\t\t\t  </div>\r\n\t\t\t\t  <div class="modal-body">\r\n\t\t\t\t\t...\r\n\t\t\t\t  </div>\r\n\t\t\t\t</div>\r\n\t\t\t  </div>\r\n\t\t\t</div>\r\n\r\n\t\t\t<!-- Modal -->\r\n\t\t\t<div class="modal fade" id="cart-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t\t\t  <div class="modal-dialog">\r\n\t\t\t\t<div class="modal-content">\r\n\t\t\t\t  <div class="modal-header">\r\n\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t\t<h4 class="modal-title" id="myModalLabel">Cart</h4>\r\n\t\t\t\t  </div>\r\n\t\t\t\t  <div class="modal-body">\r\n\t\t\t\t\t...\r\n\t\t\t\t  </div>\r\n\t\t\t\t</div>\r\n\t\t\t  </div>\r\n\t\t\t</div>\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\PycharmProjects\\ColonialHeritageFoundation\\homepage\\templates/base.htm", "line_map": {"128": 15, "192": 86, "134": 171, "16": 4, "145": 179, "18": 0, "151": 179, "157": 180, "197": 97, "163": 180, "169": 36, "42": 2, "43": 4, "44": 5, "48": 5, "200": 123, "178": 36, "179": 60, "180": 61, "53": 17, "182": 77, "183": 78, "184": 83, "57": 30, "186": 83, "187": 84, "188": 85, "189": 86, "190": 86, "181": 74, "64": 168, "193": 89, "194": 89, "195": 89, "196": 97, "69": 171, "198": 106, "199": 107, "54": 21, "74": 175, "55": 23, "206": 200, "79": 179, "56": 23, "84": 184, "89": 197, "90": 202, "91": 202, "92": 202, "58": 30, "98": 174, "59": 30, "104": 174, "110": 188, "116": 188, "122": 15}, "source_encoding": "ascii", "uri": "base.htm"}
__M_END_METADATA
"""
