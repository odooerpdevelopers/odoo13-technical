# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    report_logo = fields.Binary(string="Report Logo")
    report_logo_width = fields.Char(string="Report Logo With", default="250")
