# -*- coding: utf-8 -*-

from odoo import models, fields, api

class messages_sms(models.Model):
    _name = 'keo_marketing.sms'


    # destinataire_id = fields.One2many('mail.mass_mailing.contact', inverse_name = 'telephone', required = True)
    contact_list_ids = fields.Many2many('mail.mass_mailing.list', 'telephone', string='Liste de diffusion', required = True)
    messages_sms = fields.Text(string= "message", required = True)

    status = fields.Selection([('brouillon', 'Brouillon'), ('envoyer', 'Envoyer')], default = 'brouillon')

    programmer = fields.Datetime(string = 'planifier pour plus tard', help = 'planifier pour plus tard')




    @api.multi
    def send_sms(self):
    	if self.status == 'brouillon':
    		return self.write({'status': 'envoyer'})
    	else :
    		return { 'warning': {'title': 'brouillon', 
    					'message': 'niveau terminer'}}

        



    # send SMS with GET method
    # def send_sms(self, access_token, emetteur):
 
    #      final_url = (
    #          URL + PATH_SEND_SMS +
    #          '?accessToken=' + access_token +
    #          '&message=' + urllib.quote_plus(message.encode('iso-8859-15')) +
    #          '&numero=' + destinataires +
    #          '&emetteur=' + emetteur +
    #          '&stop=' + option_stop
    #      )
    #      r = requests.get(final_url)
    #      if not r:
    #          return ERROR_API
    #      return r.text