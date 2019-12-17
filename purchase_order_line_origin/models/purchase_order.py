# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_type = fields.Selection(
        string="Vendor Type",
        selection=[
            ('type1', 'Type1'),
            ('type2', 'Type2'),
        ]
    )


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    origin = fields.Char(string="Origin")


