# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Payroll EDI for Mexico",
    "icon": "/l10n_mx/static/description/icon.png",
    "summary": "Mexican Localization for Payroll EDI documents",
    "author": "e-maanu, "
    "Open Source Integrators, "
    "Odoo Mexican Association (AMOdoo)",
    "website": "https://github.com/amxodoo/enterprise",
    "category": "Human Resources/Payroll",
    "version": "17.0.1.0.0",
    "depends": [
        "account_edi",
        "l10n_mx_hr_payroll",
        "l10n_mx_edi_extended",
    ],
    "external_dependencies": {
        "python": ["pyOpenSSL", "zeep"],
    },
    "data": [
        "data/1.2/cfdi.xml",
        "security/ir.model.access.csv",
        "views/res_config_settings.xml",
        "views/hr_payslip.xml",
        "data/account_edi_data.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
    "assets": {},
}
