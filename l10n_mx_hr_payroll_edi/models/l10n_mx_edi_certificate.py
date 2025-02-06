# -*- coding: utf-8 -*-

import base64
import logging
import ssl
import subprocess
import tempfile
from datetime import datetime
from lxml import etree, objectify

from odoo.addons.account.tools.certificate import crypto_load_certificate

_logger = logging.getLogger(__name__)

try:
    from OpenSSL import crypto
except ImportError:
    _logger.warning('OpenSSL library not found. If you plan to use l10n_mx_edi, please install the library from https://pypi.python.org/pypi/pyOpenSSL')

from pytz import timezone

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError, UserError
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT

class Certificate(models.Model):
    _inherit = 'l10n_mx_edi.certificate'

    def get_mx_current_datetime(self):
        '''Get the current datetime with the Mexican timezone.
        '''
        return fields.Datetime.context_timestamp(
            self.with_context(tz='America/Mexico_City'), fields.Datetime.now())