# -*- coding: utf-8 -*-
{
    "name": "Lega Bagnini",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Claudio Mano",
    "website": "https://www.yourcompany.com",
    "category": "Website/Theme",
    "version": "16.0.0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "website",
        "website_sale",
        "website_event",
        "website_payment_paypal",
        "website_blog",
    ],
    # always loaded
    "data": [
        # "data/pages/homepage.xml",
        "data/pages/compile_module.xml",
        "data/images/images.xml",
    ],
}
