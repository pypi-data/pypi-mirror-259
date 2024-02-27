# Copyright 2023 Domatix - Carlos Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models
from odoo.tools.misc import get_lang


class SaleSubscriptionLine(models.Model):
    _name = "sale.subscription.line"
    _description = "Subscription lines added to a given subscription"

    product_id = fields.Many2one(
        comodel_name="product.product",
        domain=[("sale_ok", "=", True)],
        string="Product",
    )
    currency_id = fields.Many2one(
        "res.currency",
        related="sale_subscription_id.currency_id",
        store=True,
        readonly=True,
    )
    name = fields.Char(
        string="Description", compute="_compute_name", store=True, readonly=False
    )
    product_uom_qty = fields.Float(default=1.0, string="Quantity")
    price_unit = fields.Float(
        string="Unit price", compute="_compute_price_unit", store=True, readonly=False
    )
    discount = fields.Float(
        string="Discount (%)", compute="_compute_discount", store=True, readonly=False
    )
    tax_ids = fields.Many2many(
        comodel_name="account.tax",
        relation="subscription_line_tax",
        column1="subscription_line_id",
        column2="tax_id",
        string="Taxes",
        compute="_compute_tax_ids",
        store=True,
        readonly=False,
    )

    @api.depends("product_id", "price_unit", "product_uom_qty", "discount", "tax_ids")
    def _compute_subtotal(self):
        for record in self:
            price = record.price_unit * (1 - (record.discount or 0.0) / 100.0)
            taxes = record.tax_ids.compute_all(
                price,
                record.currency_id,
                record.product_uom_qty,
                product=record.product_id,
                partner=record.sale_subscription_id.partner_id,
            )
            record.update(
                {
                    "amount_tax_line_amount": sum(
                        t.get("amount", 0.0) for t in taxes.get("taxes", [])
                    ),
                    "price_total": taxes["total_included"],
                    "price_subtotal": taxes["total_excluded"],
                }
            )

    price_subtotal = fields.Monetary(
        string="Subtotal", readonly="True", compute=_compute_subtotal, store=True
    )
    price_total = fields.Monetary(
        string="Total", readonly="True", compute=_compute_subtotal, store=True
    )
    amount_tax_line_amount = fields.Float(
        string="Taxes Amount", compute="_compute_subtotal", store=True
    )
    sale_subscription_id = fields.Many2one(
        comodel_name="sale.subscription", string="Subscription"
    )
    company_id = fields.Many2one(
        related="sale_subscription_id.company_id",
        string="Company",
        store=True,
        index=True,
    )

    @api.depends("product_id")
    def _compute_name(self):
        for record in self:
            if not record.product_id:
                record.name = False
            lang = get_lang(self.env, record.sale_subscription_id.partner_id.lang).code
            product = record.product_id.with_context(lang=lang)
            record.name = product.with_context(
                lang=lang
            ).get_product_multiline_description_sale()

    @api.depends("product_id", "sale_subscription_id.fiscal_position_id")
    def _compute_tax_ids(self):
        for line in self:
            fpos = (
                line.sale_subscription_id.fiscal_position_id
                or line.sale_subscription_id.fiscal_position_id.get_fiscal_position(
                    line.sale_subscription_id.partner_id.id
                )
            )
            # If company_id is set, always filter taxes by the company
            taxes = line.product_id.taxes_id.filtered(
                lambda t: t.company_id == line.env.company
            )
            line.tax_ids = fpos.map_tax(taxes)

    @api.depends(
        "product_id",
        "sale_subscription_id.partner_id",
        "sale_subscription_id.pricelist_id",
    )
    def _compute_price_unit(self):
        for record in self:
            if not record.product_id:
                continue
            if (
                record.sale_subscription_id.pricelist_id
                and record.sale_subscription_id.partner_id
            ):
                product = record.product_id.with_context(
                    partner=record.sale_subscription_id.partner_id,
                    quantity=record.product_uom_qty,
                    date=fields.datetime.now(),
                    pricelist=record.sale_subscription_id.pricelist_id.id,
                    uom=record.product_id.uom_id.id,
                )
                record.price_unit = product._get_tax_included_unit_price(
                    record.company_id,
                    record.sale_subscription_id.currency_id,
                    fields.datetime.now(),
                    "sale",
                    fiscal_position=record.sale_subscription_id.fiscal_position_id,
                    product_price_unit=record._get_display_price(product),
                    product_currency=record.sale_subscription_id.currency_id,
                )

    @api.depends(
        "product_id",
        "price_unit",
        "product_uom_qty",
        "tax_ids",
        "sale_subscription_id.partner_id",
        "sale_subscription_id.pricelist_id",
    )
    def _compute_discount(self):
        for record in self:
            if not (
                record.product_id
                and record.product_id.uom_id
                and record.sale_subscription_id.partner_id
                and record.sale_subscription_id.pricelist_id
                and record.sale_subscription_id.pricelist_id.discount_policy
                == "without_discount"
                and self.env.user.has_group("product.group_discount_per_so_line")
            ):
                record.discount = 0.0
                continue

            record.discount = 0.0
            product = record.product_id.with_context(
                lang=record.sale_subscription_id.partner_id.lang,
                partner=record.sale_subscription_id.partner_id,
                quantity=record.product_uom_qty,
                date=fields.Datetime.now(),
                pricelist=record.sale_subscription_id.pricelist_id.id,
                uom=record.product_id.uom_id.id,
                fiscal_position=record.sale_subscription_id.fiscal_position_id
                or self.env.context.get("fiscal_position"),
            )

            price, rule_id = record.sale_subscription_id.pricelist_id.with_context(
                partner_id=record.sale_subscription_id.partner_id.id,
                date=fields.Datetime.now(),
                uom=record.product_id.uom_id.id,
            ).get_product_price_rule(
                record.product_id,
                record.product_uom_qty or 1.0,
                record.sale_subscription_id.partner_id,
            )
            new_list_price, currency = record.with_context(
                partner_id=record.sale_subscription_id.partner_id.id,
                date=fields.Datetime.now(),
                uom=record.product_id.uom_id.id,
            )._get_real_price_currency(
                product, rule_id, record.product_uom_qty, record.product_id.uom_id
            )

            if new_list_price != 0:
                if record.sale_subscription_id.pricelist_id.currency_id != currency:
                    new_list_price = currency._convert(
                        new_list_price,
                        record.sale_subscription_id.pricelist_id.currency_id,
                        record.sale_subscription_id.company_id or self.env.company,
                        fields.Date.today(),
                    )
                discount = (new_list_price - price) / new_list_price * 100
                if (discount > 0 and new_list_price > 0) or (
                    discount < 0 and new_list_price < 0
                ):
                    record.discount = discount

    def _get_real_price_currency(self, product, rule_id, qty, uom):
        PricelistItem = self.env["product.pricelist.item"]
        field_name = "lst_price"
        currency_id = None
        product_currency = product.currency_id
        if rule_id:
            pricelist_item = PricelistItem.browse(rule_id)
            if pricelist_item.pricelist_id.discount_policy == "without_discount":
                while (
                    pricelist_item.base == "pricelist"
                    and pricelist_item.base_pricelist_id
                    and pricelist_item.base_pricelist_id.discount_policy
                    == "without_discount"
                ):
                    _price, rule_id = pricelist_item.base_pricelist_id.with_context(
                        uom=uom.id
                    ).get_product_price_rule(
                        product, qty, self.sale_subscription_id.partner_id
                    )
                    pricelist_item = PricelistItem.browse(rule_id)

            if pricelist_item.base == "standard_price":
                field_name = "standard_price"
                product_currency = product.cost_currency_id
            elif (
                pricelist_item.base == "pricelist" and pricelist_item.base_pricelist_id
            ):
                field_name = "price"
                product = product.with_context(
                    pricelist=pricelist_item.base_pricelist_id.id
                )
                product_currency = pricelist_item.base_pricelist_id.currency_id
            currency_id = pricelist_item.pricelist_id.currency_id

        if not currency_id:
            currency_id = product_currency
            cur_factor = 1.0
        else:
            if currency_id.id == product_currency.id:
                cur_factor = 1.0
            else:
                cur_factor = currency_id._get_conversion_rate(
                    product_currency,
                    currency_id,
                    self.company_id or self.env.company,
                    fields.Date.today(),
                )

        product_uom = self.env.context.get("uom") or product.uom_id.id
        if uom and uom.id != product_uom:
            # the unit price is in a different uom
            uom_factor = uom._compute_price(1.0, product.uom_id)
        else:
            uom_factor = 1.0

        return product[field_name] * uom_factor * cur_factor, currency_id

    def _get_display_price(self, product):
        if self.sale_subscription_id.pricelist_id.discount_policy == "with_discount":
            return product.with_context(
                pricelist=self.sale_subscription_id.pricelist_id.id,
                uom=self.product_id.uom_id.id,
            ).price

        final_price, rule_id = self.sale_subscription_id.pricelist_id.with_context(
            partner_id=self.sale_subscription_id.partner_id.id,
            date=fields.Datetime.now(),
            uom=self.product_id.uom_id.id,
        ).get_product_price_rule(
            product or self.product_id,
            self.product_uom_qty or 1.0,
            self.sale_subscription_id.partner_id,
        )
        base_price, currency = self.with_context(
            partner_id=self.sale_subscription_id.partner_id.id,
            date=fields.Datetime.now(),
            uom=self.product_id.uom_id.id,
        )._get_real_price_currency(
            product, rule_id, self.product_uom_qty, self.product_id.uom_id
        )
        if currency != self.sale_subscription_id.pricelist_id.currency_id:
            base_price = currency._convert(
                base_price,
                self.sale_subscription_id.pricelist_id.currency_id,
                self.sale_subscription_id.company_id or self.env.company,
                fields.Date.today(),
            )
        return max(base_price, final_price)

    def _prepare_sale_order_line(self, start_date, end_date):
        self.ensure_one()
        return {
            "product_id": self.product_id.id,
            "name": self._generate_name(start_date, end_date),
            "product_uom_qty": self.product_uom_qty,
            "price_unit": self.price_unit,
            "discount": self.discount,
            "price_subtotal": self.price_subtotal,
            "tax_id": self.tax_ids,
            "product_uom": self.product_id.uom_id.id,
        }

    def _prepare_account_move_line(self, start_date, end_date):
        self.ensure_one()
        account = (
            self.product_id.property_account_income_id
            or self.product_id.categ_id.property_account_income_categ_id
        )
        return {
            "product_id": self.product_id.id,
            "name": self._generate_name(start_date, end_date),
            "quantity": self.product_uom_qty,
            "price_unit": self.price_unit,
            "discount": self.discount,
            "price_subtotal": self.price_subtotal,
            "tax_ids": [(6, 0, self.tax_ids.ids)],
            "product_uom_id": self.product_id.uom_id.id,
            "account_id": account.id,
        }

    def _generate_name(self, start_date, end_date):
        return self._insert_markers(start_date, end_date)

    def _insert_markers(self, start_date, end_date):
        self.ensure_one()
        lang_obj = self.env["res.lang"]
        lang = lang_obj.search(
            [("code", "=", self.sale_subscription_id.partner_id.lang)]
        )
        date_format = lang.date_format or "%m/%d/%Y"
        name = self.name
        name = name.replace("#START#", start_date.strftime(date_format))
        name = name.replace("#END#", end_date.strftime(date_format)) if end_date else ""
        name = name.replace("#INVOICEMONTHNUMBER#", start_date.strftime("%m"))
        name = name.replace("#INVOICEYEAR#", start_date.strftime("%Y"))
        name = name.replace(
            "#INVOICEMONTHNAME#",
            self.with_context(lang=lang.code)._translate_marker_month_name(
                start_date.strftime("%m")
            ),
        )
        return name

    def _translate_marker_month_name(self, month_name):
        months = {
            "01": _("January"),
            "02": _("February"),
            "03": _("March"),
            "04": _("April"),
            "05": _("May"),
            "06": _("June"),
            "07": _("July"),
            "08": _("August"),
            "09": _("September"),
            "10": _("October"),
            "11": _("November"),
            "12": _("December"),
        }
        return months[month_name]
