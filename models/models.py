# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Socio(models.Model):
 _name = 'cdpelotas3763_y.socios'

 num_socio = fields.Integer(string="Numero de socio")
 nombre = fields.Char(string="Nombre")
 apellidos = fields.Char(string="Apellidos")
 direccion = fields.Char(string="Direccion")
 telefono = fields.Integer(string="Teléfono")
 fecha_alta = fields.Date(string="Fecha de Alta")