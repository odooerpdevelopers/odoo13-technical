# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    price_with_discount = fields.Float(
        string="Precio + descuento",
        compute="_get_price_discount",
        default=0
    )

    @api.depends("product_id", "product_tmpl_id")
    def _get_price_discount(self):
        for line in self:
            if line.compute_price == "percentage":
                tmpl_id = line.product_tmpl_id
                if not tmpl_id:
                    tmpl_id = line.product_id.product_tmpl_id
                discount = (tmpl_id.list_price * line.percent_price) / 100
                final_price = tmpl_id.list_price - discount
                line.price_with_discount = final_price
            else:
                line.price_with_discount = 0.00
