# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import io

from lxml import etree, objectify
from os.path import join
from werkzeug.urls import url_quote

from odoo import api, models, tools


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def l10n_mx_edi_validate_xml_from_attachment(self, xml_content, xsd_name):
        tools.validate_xml_from_attachment(self.env, xml_content, xsd_name, prefix='l10n_mx_edi')
