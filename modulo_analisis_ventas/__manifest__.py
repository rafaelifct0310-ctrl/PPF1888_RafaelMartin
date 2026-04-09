# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Analisis de Ventas PPF1888',
    'version': '19.0.1.0.0',
    'category': 'Sales/Reporting',
    'summary': 'Informe de análisis de ventas',
    'description': """
Módulo básico para consultas e informes de análisis de ventas, incluyendo el informe de ventas por producto y el informe de ventas por cliente.
    """,
    'author': 'Rafael Martín',
    'license': 'LGPL-3',
    'depends': ['sales'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_report_views.xml',
        'report/sale_report_views.xml',
        'report/sale_report_templates.xml',
    ],
    'demo': [
        'data/product_demo.xml',
        'data/sale_demo.xml',
    ],
    'installable': True,
    'application': False,
     
}
    
    
