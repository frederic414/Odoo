# -*- coding: utf-8 -*-

from odoo import models, fields, api

class client(models.Model):
	
	_inherit = 'res.partner'


	numero_cnib = fields.Char(string = "numero cnib", help = "Veuillez entrer votre numero CNIB")
	numeo_ifu = fields.Char(string = "numero IFU", help = "Veuillez entrer votre numero IFU")



