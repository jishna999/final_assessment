
from odoo import models, fields, api


class DayWiseReport(models.TransientModel):
    _name = 'day.report'
    _description = 'Day wise Report'

    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    company_id =fields.Many2many(comodel_name='res.company')

    def action_report(self):
        return True