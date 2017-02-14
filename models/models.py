# -*- coding: utf-8 -*-

from openerp import models, fields, api

class source(models.Model):
    _name = 'syncid.source'

    name = fields.Char()

class reference(models.Model):
    _name = 'syncid.reference'

    def object(self):
        # TODO: check this!
        obj = selv.env[sel.model.name].browse(self.odoo_id)
        return obj

    model = fields.Many2One('ir.models')
    source = fields.Many2One('syncid.source')
    odoo_id = fields.Integer()
    source_id = fields.Char()
