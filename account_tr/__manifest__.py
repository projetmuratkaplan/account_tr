{
    'name': 'Account Turkey Localization',
    'version': '16.0.0.1',
    'license': 'LGPL-3',
    'category': 'Localization/Turkey',

    'author': 'Odoo Premium',
    'website': 'https://www.odoopremium.com/app/account_tr',

    'depends': ['account_tr_base'],

    'data': [        
        'security/ir.model.access.csv',
        'data/res_banks_tr.xml', 

        'data/account_chart_template_data.xml',
        'data/account_group_template.xml',
        'data/account_account_template.xml',
        'data/account_chart_template_post_data.xml',
        'data/account_fiscal_position_category.xml',
        'data/account_tag_template_data.xml',
        'data/account_tax_group_template.xml',

        'data/account_tax_template_base_tax_data.xml',
        'data/account_tax_template_data_18.xml',
        'data/account_tax_template_data_20.xml',

        'data/account_reconcile_model_template.xml',

        'data/account_fiscal_position_template_1xx.xml',
        'data/account_fiscal_position_template_2xx.xml',
        'data/account_fiscal_position_template_3xx.xml',
        'data/account_fiscal_position_template_4xx.xml',
        'data/account_fiscal_position_template_5xx.xml',
        'data/account_fiscal_position_template_6xx.xml',
        'data/account_fiscal_position_template_7xx.xml',
        'data/account_fiscal_position_template_8xx.xml',

        'data/account_fiscal_position_account_template.xml',

        'data/account_fiscal_position_tax_template.xml',
        'data/account_fiscal_position_tax_template_new.xml',

        'data/account_fiscal_position_tax_template_3xx.xml',
        'data/account_fiscal_position_tax_template_3xx_new.xml',

        'data/account_fiscal_position_tax_template_2xx.xml',
        'data/account_fiscal_position_tax_template_2xx_new.xml',

        'data/account_fiscal_position_tax_template_8xx.xml',
        'data/account_fiscal_position_tax_template_8xx_new.xml',

        'data/account_chart_template_configure_data.xml',

        'views/account_fiscal_position_template.xml',
        'views/account_fiscal_position_category.xml',
        'views/account_fiscal_position.xml',

        'views/account_tax.xml', 
        'views/account_journal.xml',
        'views/res_bank.xml',
        'views/res_company.xml',
        'views/account_tax_template.xml'
    ],

    'post_init_hook': 'post_init_hook',

    #'assets': {
    #    'web.assets_backend': [''],
    #    'web.assets_qweb': [''],
    #},

    'demo': [],

    'tests': [],

    'maintainer': 'Odoo Premium',
    'url': 'https://github.com/odoopremium/account/tree/16.0',
    'live_test_url': 'https://runbot16.odoopremium.com',

    'sequence': 1,
    'installable': True,
    'application': True,
    'auto_install': False,

    #'external_dependencies': {'python': []}
}
