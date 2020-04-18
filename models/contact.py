# -*- coding: utf-8 -*-

from odoo import models, fields, api

class contact(models.Model):
    _name = 'mail.mass_mailing.contact'
    _inherit = 'mail.mass_mailing.contact'


    telephone = fields.Char(string = 'téléphone', required = True, help = 'Entrer votre numero de téléphone')
    