{
    "name": "TrackMyFleet",
    'summary': 'A module for managing our fleet and records about vehicles from our fleet who need to be maintained',
    'author': 'Moldovan Alex',
    'version': '17.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Fleet',
    'depends': ['base', "fleet", "account", "account_fleet"],
    'data':[
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/fleet_maintenance_views.xml',
        'views/fleet_maintenance_menus.xml'
    ],
    'demo':[
        "demo/demo.xml"
    ],
    'installable' : True,
    'application': True
}