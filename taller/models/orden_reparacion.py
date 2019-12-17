# -*- coding: utf-8 -*-

from odoo import api, models, fields


class OrderReparacion(models.Model):
    _name = 'taller.orden.reparacion'
    _description = 'Gestion Ordenes Reparacion'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        default="Nueva Orden Reparacion")
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Cliente")

    reparacion_line_ids = fields.One2many(
        comodel_name="taller.orden.reparacion.line",
        inverse_name="reparacion_id",
        string="lineas Reparacion"
    )

    @api.model
    def create(self, vals):
        new_seq_name = self.env['ir.sequence'].next_by_code(
            'orden.reparacion') or 'New'
        vals.update(name=new_seq_name)
        res = super(OrderReparacion, self).create(vals)
        return res


class OrderReparacionLine(models.Model):
    _name = 'taller.orden.reparacion.line'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        default="Nueva Linea Reparacion")
    reparacion_id = fields.Many2one(comodel_name="taller.orden.reparacion")
    vehiculo_id = fields.Many2one(
        comodel_name="taller.vehiculo", string="Vehiculo")

