# from odoo import http


# class WebsiteLegaBagnini(http.Controller):
#     @http.route("/website_lega_bagnini/website_lega_bagnini", auth="public")
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route("/website_lega_bagnini/website_lega_bagnini/objects", auth="public")
#     def list(self, **kw):
#         return http.request.render(
#             "website_lega_bagnini.listing",
#             {
#                 "root": "/website_lega_bagnini/website_lega_bagnini",
#                 "objects": http.request.env[
#                     "website_lega_bagnini.website_lega_bagnini"
#                 ].search([]),
#             },
#         )

#     @http.route(
#         "/website_lega_bagnini/website_lega_bagnini/objects/"
#         "<model('website_lega_bagnini.website_lega_bagnini'):obj>",
#         auth="public",
#     )
#     def object(self, obj, **kw):
#         return http.request.render("website_lega_bagnini.object", {"object": obj})
