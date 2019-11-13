# -*- coding: utf-8 -*-

from openerp import models, fields, api

class source(models.Model):
    _name = 'syncid.source'

    name = fields.Char()

class reference(models.Model):
    _name = 'syncid.reference'

    def object(self):
        # TODO: check this!
        obj = self.env[self.model.model].browse(self.odoo_id)
        return obj

    model = fields.Many2one('ir.model', required=True)
    source = fields.Many2one('syncid.source', required=True)
    odoo_id = fields.Integer(required=True, index=True)
    source_id = fields.Char(required=True, index=True)
    scope = fields.Char(index=True)