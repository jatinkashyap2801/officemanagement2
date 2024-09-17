from odoo import models,fields
class Department(models.Model):
    _inherit="hr.department"
    employees=fields.Many2many('hr.employee',string="Employees",can_create=False)