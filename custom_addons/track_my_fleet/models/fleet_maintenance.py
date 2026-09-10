from odoo import models, fields, api
from datetime import date

class FleetMaintenance(models.Model):
    _name = "fleet.maintenance"
    _description = "First module"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
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

    def write(self, vals):
        res = super(FleetMaintenance, self).write(vals)
        if 'stage' in vals and vals['stage'] == 'needs_parts':
            for record in self:
                record.activity_schedule(
                    'mail.mail_activity_data_todo',
                    summary=f"Procurement required for {record.vehicle_id.display_name}",
                    note=f"Defect type: {record.defect_type}. Please order necessary parts.",
                    user_id=self.env.uid,
                )
        return res

    def action_trigger_procurement_task(self):
        self.write({'stage': 'needs_parts'})
            
    @api.model
    def _cron_send_overdue_maintenance_email(self):
        today = date.today()
        overdue_records = self.search([
            ('stage', '!=', 'completed'),
            ('target_date', '<', today)
        ])
        if not overdue_records:
            return
        coordinator_group = self.env.ref('fleet.fleet_group_manager', raise_if_not_found=False)
        recipients = coordinator_group.users.mapped('email') if coordinator_group else []
        email_to = ",".join(filter(None, recipients)) or self.env.company.email
        template = self.env.ref('track_my_fleet.email_template_overdue_maintenance', raise_if_not_found=False)
        if template and email_to:
            template.with_context(overdue_records=overdue_records).send_mail(
                self.env.user.id,
                force_send=True,
                email_values={'email_to': email_to}
            )