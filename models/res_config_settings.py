from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    wa_provider = fields.Selection(
        selection=[('360dialog', '360dialog'), ('unoapi', 'UNO API')],
        string="WhatsApp Provider",
        related='company_id.wa_provider',
        readonly=False,
    )
    wa_base_url = fields.Char(
        string="Provider Base URL",
        related='company_id.wa_base_url',
        readonly=False,
    )
    wa_api_key_header = fields.Char(
        string="API Key Header",
        related='company_id.wa_api_key_header',
        readonly=False,
    )
    wa_api_version = fields.Char(
        string="API Version",
        related='company_id.wa_api_version',
        readonly=False,
    )
    wa_phone_number_id = fields.Char(
        string="Phone Number ID",
        related='company_id.wa_phone_number_id',
        readonly=False,
    )

    dialog_api_key = fields.Char(
        string="360 Dialog Api Key",
        help="API key 360 Dialog para WhatsApp",
        related='company_id.dialog_api_key',
        readonly=False,
    )
    dialog_namespace = fields.Char(
        string="360 NameSpace",
        help="NameSpace 360 Dialog para WhatsApp",
        related='company_id.dialog_namespace',
        readonly=False,
    )
    webhook_url = fields.Char(
        string="360 WebHook Address",
        help="NameSpace 360 Dialog para WhatsApp",
        related='company_id.webhook_url',
        readonly=False,
    )
    developer_mode = fields.Boolean(
        related='company_id.developer_mode',
        readonly=False,
    )


class Company(models.Model):
    _inherit = "res.company"

    wa_provider = fields.Selection(
        selection=[('360dialog', '360dialog'), ('unoapi', 'UNO API')],
        string="WhatsApp Provider",
        default='360dialog',
    )
    wa_base_url = fields.Char(
        string="Provider Base URL",
    )
    wa_api_key_header = fields.Char(
        string="API Key Header",
        default='Authorization',
    )
    wa_api_version = fields.Char(
        string="API Version",
        default='v19.0',
    )
    wa_phone_number_id = fields.Char(
        string="Phone Number ID",
    )
    dialog_api_key = fields.Char(
        string="360 Dialog Api Key",
    )
    dialog_namespace = fields.Char(
        string="360 NameSpace",
    )
    webhook_url = fields.Char(
        string="360 NameSpace",
    )
    developer_mode = fields.Boolean(
        string="Developer Mode"
    )
