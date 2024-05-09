# from odoo import models, fields, api


# class website_lega_bagnini(models.Model):
#     _name = 'website_lega_bagnini.website_lega_bagnini'
#     _description = 'website_lega_bagnini.website_lega_bagnini'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
