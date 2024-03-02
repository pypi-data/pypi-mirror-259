# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class PropertyObject(models.Model):
    _name = "property_object"
    _inherit = ["property_object"]

    allowed_warehouse_ids = fields.Many2many(
        string="Allowed Warehouses",
        comodel_name="stock.warehouse",
        compute="_compute_allowed_warehouse_ids",
        store=False,
        compute_sudo=True,
    )
    warehouse_id = fields.Many2one(
        string="Warehouse",
        comodel_name="stock.warehouse",
        ondelete="restrict",
    )
    allowed_location_ids = fields.Many2many(
        string="Allowed Locations",
        comodel_name="stock.location",
        compute="_compute_allowed_location_ids",
        store=False,
        compute_sudo=True,
    )
    location_id = fields.Many2one(
        string="Location",
        comodel_name="stock.location",
        ondelete="restrict",
    )

    @api.depends(
        "need_parent",
        "warehouse_id",
    )
    def _compute_allowed_location_ids(self):
        location_type_root = self.env.ref("ssi_stock.location_type_root")
        location_type_main_stock = self.env.ref("ssi_stock.location_type_main_stock")
        location_type_stock = self.env.ref("ssi_stock.location_type_stock")
        for record in self:
            result = []
            if record.warehouse_id:
                criteria = [("warehouse_id", "=", record.warehouse_id.id)]
                if not record.need_parent:
                    criteria += [
                        ("type_id", "=", location_type_root.id),
                    ]
                else:
                    criteria += [
                        "|",
                        ("type_id", "=", location_type_main_stock.id),
                        ("type_id", "=", location_type_stock.id),
                    ]
                result = self.env["stock.location"].search(criteria).ids
            record.allowed_location_ids = result

    @api.depends(
        "parent_id",
    )
    def _compute_allowed_warehouse_ids(self):
        for record in self:
            criteria = []
            if record.parent_id:
                criteria = [
                    ("id", "=", record.parent_id.warehouse_id.id),
                ]
            record.allowed_warehouse_ids = (
                self.env["stock.warehouse"].search(criteria).ids
            )

    @api.onchange(
        "type_id",
        "parent_id",
    )
    def onchange_warehouse_id(self):
        self.warehouse_id = False

    @api.onchange(
        "warehouse_id",
    )
    def onchange_location_id(self):
        self.location_id = False
