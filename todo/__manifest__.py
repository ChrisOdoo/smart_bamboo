{
    'name': 'Tareas',
    'version': '1.0',
    'summary': 'Gestión de Tareas',
    'description': 'Módulo para gestionar tareas con CRUD básico.',
    'author': 'Ing Chris Padilla',
    'website': 'https://www.linkedin.com/in/christian-padilla-194006a7/',
    'category': 'Productivity smart bamboo 2025',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tareas_views.xml',
        'views/tareas_menu.xml', 
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

