from odoo import models, fields, api

class source(models.Model):
    _name = 'syncid.source'
    _description = 'syncid source model'

    name = fields.Char()

class reference(models.Model):
    _name = 'syncid.reference'
    _description = 'syncid reference model'


    def object(self):
        # TODO: check this!
        obj = self.env[self.model.name].browse(self.odoo_id)
        return obj

    model = fields.Many2one('ir.model')
    source = fields.Many2one('syncid.source')
    odoo_id = fields.Integer()
    source_id = fields.Char(index=True)
    scope = fields.Char(index=True)
