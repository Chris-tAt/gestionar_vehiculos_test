from odoo import models, fields

class Vehicle(models.Model):
    _name = 'reception_car.vehicle'
    _description = 'Vehículo'

 
    diagnostic_ids = fields.One2many('reception_car.diagnostic', 'vehicle_id', string='Diagnósticos')
    mileage_record_ids = fields.One2many('reception_car.mileage_record', 'vehicle_id', string='Registros de Kilometraje')

    # Campos para datos del cliente
    client_name = fields.Char(string='Cliente')
    phone = fields.Char(string='Teléfono')
    address = fields.Char(string='Dirección')
    vin = fields.Char(string='VIN')
    quotation = fields.Char(string='Cotización')

    # Campos para datos del vehículo
    model = fields.Char(string='Modelo')
    plate = fields.Char(string='Placa')
    plate_expiry = fields.Date(string='Vencimiento de Placa')
    brand = fields.Char(string='Marca')
    year = fields.Integer(string='Año del Carro')
    comments = fields.Text(string='Comentarios')