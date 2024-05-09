{
    "name": "Lega Bagnini",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "author": "Claudio Mano",
    "website": "https://github.com/OCA/lega-bagnini",
    "category": "Website/Theme",
    "version": "16.0.0.0.1",
    "license": "LGPL-3",
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
