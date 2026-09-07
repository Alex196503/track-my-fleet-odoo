from odoo import models, fields

class FleetMaintenance(models.Model):
    _name = "fleet.maintenance"
    _description = "First module"
    name = fields.Char(required = True, string = "Name")
    vehicle_id = fields.Many2one("fleet.vehicle", string = "Vehicle", required = True)
    mileage = fields.Integer(string='Mileage at Service', required=True)
    defect_type = fields.Selection([('engine', 'Engine'),
        ('brakes', 'Brakes'),
        ('electrical', 'Electrical'),
        ('tires', 'Tires'),
        ('other', 'Other')], string= "Defect Type", required = True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Urgent')
    ], string='Priority', default='0')
    tehnician = fields.Many2one('res.users', string = "Tehnician")
    target_date = fields.Date(string='Target Completion Date')
    stage = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('needs_parts', 'Needs Parts'),
        ('completed', 'Completed')
    ], string='Status', default='draft')
    estimated_down_time = fields.Float(string="Estimated Down Time (Hours)", digits=(16, 2))
    service_cost = fields.Float(string="Cost (EUR)", digits=(16, 2))
