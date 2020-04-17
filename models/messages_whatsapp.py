# -*- coding: utf-8 -*-

from odoo import models, fields, api

class messages_whatsapp(models.Model):
    _name = 'keo_marketing.whatsapp'


    destinataires = fields.Many2one(comodel_name= "mail.mass_mailing.contact", required = True)
    messages_whatsapp = fields.Text(string= "message", required = True)

    status = fields.Selection([('brouillon', 'Brouillon'), ('envoyer', 'Envoyer')])