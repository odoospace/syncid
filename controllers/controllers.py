# -*- coding: utf-8 -*-
from odoo import http

# class syncid(http.Controller):
#     @http.route('/syncid/syncid/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syncid/syncid/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syncid.listing', {
#             'root': '/syncid/syncid',
#             'objects': http.request.env['syncid.syncid'].search([]),
#         })

#     @http.route('/syncid/syncid/objects/<model("syncid.syncid"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syncid.object', {
#             'object': obj
#         })
