from odoo import fields, models, api


class hh(models.Model):
    _name = 'medical.tab'
    _description = 'Description'

    name = fields.Char()
