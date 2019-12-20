# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
import logging
import base64
import csv
import io

_logger = logging.getLogger(__name__)

from odoo import api, models, fields, exceptions


class ImportBoMWizard(models.TransientModel):
    _name = 'import.bom.wizard'

    file_type = fields.Selection(
        selection=[
            ('csv', 'Archivo CSV'),
        ],
        default="csv",
        required=True,
        string="Tipo de archivo"
    )

    product_id = fields.Many2one(
        'product.template',
        string='Producto'
    )

    routing_id = fields.Many2one(
        'mrp.routing',
        string='Ruta'
    )

    file_data = fields.Binary('Archivo', required=True)

    @api.model
    def default_get(self, fields_list):
        res = super(ImportBoMWizard, self).default_get(fields_list)
        if self._context.get("active_id"):
            res.update(product_id=self._context.get("active_id"))
        return res

    def import_bom(self):

        bom = self.env['mrp.bom']
        product = self.env['product.product']

        try:
            decoded_data = base64.decodebytes(self.file_data).replace(
                b'\xef\xbb\xbf', b'').replace(b';', b',')
            f = io.TextIOWrapper(io.BytesIO(decoded_data), encoding='utf-8')
            reader = csv.DictReader(f, delimiter=',')
        except Exception:
            raise ValidationError(
                "No se ha podido cargar el fichero.\n El fichero debe ser de "
                "tipo {}.".format(
                    self.file_type.upper()))

        bom_ids = []
        for row in reader:
            cols = dict(row)

            code = cols.get('Code', False)
            cantidad = cols.get('Cantidad', False)

            if not code or not cantidad:
                raise ValidationError(
                    "El fichero no contiene una lista de materiales válida.")

            pro = product.search([('default_code', '=', code)])
            if pro:
                bom_ids.append((0, 0, {'product_id': pro.id, 'product_qty': cantidad, 'product_uom_id': pro.uom_id.id}))
            else:
                raise ValidationError(
                    "El producto con code: {} no existe.".format(
                        code))

        if bom_ids:
            bom_to_create = {
                # 'product_id': self.product_id.product_variant_id.id,
                'product_tmpl_id': self.product_id.id,
                'product_uom_id': self.product_id.uom_id.id,
                'product_qty': 1.0,
                'routing_id': self.routing_id.id,
                'type': 'normal',
                'ready_to_produce': 'asap',
                'bom_line_ids': bom_ids
            }

            res = bom.create(bom_to_create)
            _logger.info(
                "Se ha generado la LdM {} para el producto {}".format(
                    res.id,
                    self.product_id.name))
        else:
            raise ValidationError(
                "El archivo CSV proporcionado no ha generado ninguna lista "
                "de materiales válida.")

        return {}
