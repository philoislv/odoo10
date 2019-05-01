# -*- coding: utf-8 -*-
from odoo import models, fields, api
#Modelo Socio
class Socio(models.Model):
 _name = 'cdpelotas3763_y.socios'

 num_socio = fields.Integer(string="Numero de socio")
 nombre = fields.Char(string="Nombre")
 apellidos = fields.Char(string="Apellidos")
 direccion = fields.Char(string="Direccion")
 telefono = fields.Integer(string="Teléfono")
 fecha_alta = fields.Date(string="Fecha de Alta")
 #Campo reservas
 #Modelo Instalaciones
class Instalaciones(models.Model):
 _name = 'cdpelotas3763_y.instalaciones'
 num_pista = fields.Integer(string="Numero de pista")
 nombre_pista = fields.Char(string="Nombre de Pista")
 superficie = fields.Selection([('cemento','Cemento'),('hierba','Hierba'),('moqueta','Moqueta'),('tierra','Tierra')])
 luz = fields.Selection([('si','Si'),('no','No')])
 precio = fields.Integer(string="Precio/hora de la pista")
 estado = fields.Selection([('disponible','Disponible'),('mantenimiento','Mantenimiento')])
 #Campo deporte
 #Campo reservas