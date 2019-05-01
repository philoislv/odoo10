# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class cdpelotas3763_y(models.Model):
#     _name = 'cdpelotas3763_y.cdpelotas3763_y'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Socio(models.Model):
 _name = 'cdpelotas3763_y.socios'

 num_socio = fields.Integer(string="Numero de socio")
 nombre = fields.Char(string="Nombre")
 apellidos = fields.Char(string="Apellidos")
 direccion = fields.Text(string="Direccion")
 telefono = fields.Integer(string="Teléfono")
 fecha_alta = fields.Text(string="Fecha de Alta")
 @api.depends('value')
 def _value_pc(self):
  self.value2 = float(self.value) / 100