from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    part_number = fields.Char(
        string='Part Number',
        related='product_id.default_code',
        readonly=True,
    )
