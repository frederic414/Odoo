# -*- coding: utf-8 -*-

from odoo import models, fields, api

class keo_marketing(models.Model):
    _name = 'keo_marketing.keo_marketing'


    destinataires = fields.Many2one(comodel_name= "mail.mass_mailing.contact", required = True)
    messages_whatsapp = fields.Text(string= "message", required = True)

    stat = fields.Selection([('brouillon', 'Brouillon'), ('envoyer', 'Envoyer')], default = 'brouillon')