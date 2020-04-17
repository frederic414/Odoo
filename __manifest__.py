# -*- coding: utf-8 -*-
{
    'name': "Keo Marketing",

    'summary': """
        Module de marketing""",

    'description': """
        KeoMarketing est un module 3 en 1 qui vous offre la possibilité de faire vos 
        campaganes marketing via email, sms oubien les messages whatsapp
    """,

    'author': "KeoLID Innovation Hub",
    'website': "http://www.keolid.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail_bot', 'mail', 'mass_mailing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/publipostage_views.xml',
        'views/sms_views.xml',
        'views/contacts_view.xml',
        'views/clients_view.xml',
        'views/diffusion_views.xml',
        'views/whatsapp_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}