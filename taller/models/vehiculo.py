# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Vehicle(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Gestion Vehiculos Odoo'

    name = fields.Char(string="Name", help="Introduce el nombre", size=20,
                       default="Nuevo")
    active = fields.Boolean(string="Active", default=True)
    matricula = fields.Char("Placa")

    _sql_constraints = [
        ('vehiculo_name_uniq',
         'unique (name)',
         'Nombre tiene que ser unico.')
    ]

    @api.constrains('matricula')
    def _check_matricula(self):
        # comoprobamos que sea unica
        domain = [
            ('matricula', '=', self.matricula),
            ('id', '!=', self.id),
        ]
        vehiculos = self.search(domain)
        if vehiculos:
            raise exceptions.ValidationError("Matricula duplicada")
