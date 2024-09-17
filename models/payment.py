from odoo import models , fields,api
from odoo.exceptions import ValidationError
class Payment(models.Model):
    _inherit="account.payment"

    employee=fields.Many2one('hr.employee',string="Employee" ,placeholder="Employee")
    e_name=fields.Char(string="name")

    @api.model
    def create(self,vals):
        if vals.get('employee'):
            rec=vals.get('employee')
            record=self.env['hr.employee'].search([('id','=',rec)])
            if record:
                vals['amount']=record.salary
        return super(Payment,self).create(vals)


    # @api.onchange('e_name')
    # def _compute_amount(self):
    #     for record in self:
    #         if record.e_name:
    #             emp=self.env['hr.employee'].search([('name','=',record.e_name)],limit=1);
    #             if emp:
    #                 # record.amount=emp.salary
    #                 self.write({'amount':emp.salary})



    
    # amount=fields.Monetary(compute="_compute_amount",store=True)

    # @api.depends('e_name')
    # def _compute_amount(self):
    #     for record in self:
    #         if record.e_name:
    #             emp=self.env['hr.employee'].search([('name','=',record.e_name)],limit=1)
    #             if emp:
    #                 record.amount=emp.salary






    # @api.model
    # def create(self,vals):
    #     if vals.get('e_name'):
    #         emp=vals.get('e_name');
    #         record = self.env['hr.employee'].search([('name','=',emp)],limit=1);
    #         if record:
    #             vals['amount']=record.salary
    #     else:
    #         raise ValidationError("no emp")
    #     return super(Payment,self).create(vals)

    # def write(self,vals):
    #     emp=vals.get('e_name');
    #     # if emp:
    #     record=self.env['hr.employee'].search([('name','=',emp)],limit=1)
    #     if record:
    #         vals['amount']=record.salary
    #     else:
    #         raise ValidationError("error 1")
    #     return super(Payment,self).write(vals)

    def action_pay(self):
        if not self.employee:
            raise ValidationError("Please select an employee.")
        return {
            'name': 'Confirm Payment',
            'type': 'ir.actions.act_window',
            'res_model': 'pay.conf',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_employee': self.employee.id,
                'default_amount': self.amount,
                'active_id': self.id,
            }
        }