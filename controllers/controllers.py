# -*- coding: utf-8 -*-
from odoo import http

# class KeoMarketing(http.Controller):
#     @http.route('/keo_marketing/keo_marketing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/keo_marketing/keo_marketing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('keo_marketing.listing', {
#             'root': '/keo_marketing/keo_marketing',
#             'objects': http.request.env['keo_marketing.keo_marketing'].search([]),
#         })

#     @http.route('/keo_marketing/keo_marketing/objects/<model("keo_marketing.keo_marketing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('keo_marketing.object', {
#             'object': obj
#         })