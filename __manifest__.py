{
    'name': "SyncID",

    'summary': """
        Module to support external ids to odoo model objects""",

    'description': """
        Module to support external ids to odoo model objects
    """,

    'author': "Impulso Diagonal",
    'website': "http://www.impulso.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
