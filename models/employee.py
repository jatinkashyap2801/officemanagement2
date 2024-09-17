from odoo import models,fields
class Employees(models.Model):
    _inherit="hr.employee"
    attend=fields.Char()
    salary = fields.Float(string='Salary')
    expected_appraisal = fields.Float(string='Expected Appraisal')