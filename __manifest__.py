# -*- coding: utf-8 -*-
{
    'name': 'WhatsApp API Integration (360dialog/UNO)',
    'summary': "Send and receive WhatsApp messages via 360dialog or UNO API",
    'description': """
Integrates Odoo with 360dialog or UNO API (Meta-like compatibility).
Features:
 - Send WhatsApp messages from CRM/Leads, Partners, and custom models.
 - Manage WhatsApp message templates and parameters.
 - Webhook for receiving incoming WhatsApp messages.
 - Configuration panel under Settings > WhatsApp.
    """,
    'author': 'ChatWithIO (maintained by 360 Aviation Life)',
    'website': 'https://360aviationlife.com',
    'support': 'info@chatwithio.com',
    'category': 'Productivity/Messaging',
    'version': '18.0.1.0.0',
    'depends': [
        'mail',
        'crm',
        'base_setup',   # needed for res.config.settings inheritance
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_lead_adaptation.xml',
        'data/activity_type_data.xml',
        'views/whatsapp_views.xml',
        'views/whatsapp_adaptation_model_views.xml',
        'views/whatsapp_template_views.xml',
        'views/mail_template_views.xml',
        'views/res_config_settings_view.xml',
        'wizards/mail_compose_message_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # if you add JS or CSS in the future
            # 'odoo_whatsapp_api/static/src/js/whatsapp_widget.js',
        ],
    },
    'license': "LGPL-3",
    'auto_install': False,
    'installable': True,
    'application': True,
}
