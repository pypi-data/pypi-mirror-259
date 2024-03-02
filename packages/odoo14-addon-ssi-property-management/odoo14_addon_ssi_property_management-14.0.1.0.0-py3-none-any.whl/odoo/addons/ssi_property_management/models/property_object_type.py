# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PropertyObjectType(models.Model):
    _name = "property_object_type"
    _inherit = ["mixin.master_data"]
    _description = "Property Object Type"

    allowed_parent_type_ids = fields.Many2many(
        string="Allowed Parent Types",
        comodel_name="property_object_type",
        relation="rel_property_object_type_2_parent",
        column1="type_id",
        column2="parent_type_id",
    )
    need_parent = fields.Boolean(
        string="Need Parent",
    )
