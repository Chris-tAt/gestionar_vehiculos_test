from odoo import models, fields

class Diagnostic(models.Model):
    _name = 'reception_car.diagnostic'
    _description = 'Diagnóstico'

    # Agregar el campo 'vehicle_id'
    vehicle_id = fields.Many2one('reception_car.vehicle', string='Vehículo')

    # Campos para el diagnóstico
    date = fields.Date(string='Fecha')
    responsible = fields.Many2one('res.users', string='Encargado')
    area = fields.Char(string='Área')
    services = fields.Many2many('your.service.model', string='Servicios')
    code = fields.Char(string='Código')
    comment = fields.Text(string='Comentario')
    hours = fields.Float(string='Horas')
    to_quote = fields.Boolean(string='Cotizar')

class MileageRecord(models.Model):
    _name = 'reception_car.mileage_record'
    _description = 'Registro de Kilometraje'

    # Agregar el campo 'vehicle_id'
    vehicle_id = fields.Many2one('reception_car.vehicle', string='Vehículo')

    # Campos para el registro de kilometraje
    date = fields.Date(string='Fecha')
    mileage = fields.Float(string='Kilometraje')
    responsible = fields.Many2one('res.users', string='Encargado')