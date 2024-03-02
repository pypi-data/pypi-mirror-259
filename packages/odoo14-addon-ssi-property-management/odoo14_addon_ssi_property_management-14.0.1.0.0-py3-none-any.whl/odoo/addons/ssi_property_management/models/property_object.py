# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PropertyObject(models.Model):
    _name = "property_object"
    _inherit = ["mixin.master_data"]
    _description = "Property Object"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="property_object_type",
        required=True,
        ondelete="restrict",
    )
    parent_id = fields.Many2one(
        string="Parent Property",
        comodel_name="property_object",
        ondelete="restrict",
    )
    need_parent = fields.Boolean(
        related="type_id.need_parent",
        store=False,
    )
    child_ids = fields.One2many(
        string="Child Properties",
        comodel_name="property_object",
        inverse_name="parent_id",
    )
    allowed_parent_type_ids = fields.Many2many(
        related="type_id.allowed_parent_type_ids",
        store=False,
    )
