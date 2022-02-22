# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology(models.Model):
    _name = 'medical.pathology'

    name = fields.Char(string="Name",required=True)
    code = fields.Char(string="Code")
    category_id = fields.Many2one('medical.pathology.category',string="Disease Category")
    line_ids = fields.One2many('medical.pathology.group.member','disease_group_id',string="Group")
    chromosome = fields.Char(string="Affected Chromosome")
    gene = fields.Char(string="Gene")
    protein = fields.Char(string="Protein")
    info = fields.Text(string="Extra Info")
    pathology_count = fields.Integer(compute='pathology_compute_count')

    def pathology_compute_count(self):
        for record in self:
            record.pathology_count = self.env['medical.patient.disease'].search_count(
                [('pathology_id', '=', self.id)])

    def get_patient(self):
        return {
            'name': _('Patient'),
            'view_type':'form',
            'res_model':'medical.patient.disease',
            'view_id':False,
            'view_mode':'tree,form',
            'type':'ir.actions.act_window',
            'domain': [('pathology_id', '=', self.id)],
            'context': {'default_pathology_id': self.id},

        }