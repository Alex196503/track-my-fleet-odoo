{
    "name": "TrackMyFleet",
    'summary': 'A module for managing our fleet and records about vehicles from our fleet who need to be maintained',
    'author': 'Moldovan Alex',
    'version': '17.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Fleet',
    'depends': ['base', "fleet", "account", "account_fleet", "mail"],
    'data':[
        'security/res_groups.xml',
        "data/mail_template_data.xml",
        'data/cron_data.xml',
        'security/ir.model.access.csv',
        'views/fleet_maintenance_views.xml',
        'views/fleet_maintenance_menus.xml'
    ],
    'demo':[
        "demo/demo.xml"
    ],
    'assets':{
        'web.assets_backend':[
        'track_my_fleet/static/src/components/maintenance_summary.js',
        'track_my_fleet/static/src/components/maintenance_summary.xml',
        ]
    },
    'installable' : True,
    'application': True
}