{
    'name': "Library Management",
    "description": "Library Management",
    "version": "14.0.0.1.0",
    "category": "Management",
    "website": "https://www.aktivsoftware.com/",
    "depends": ['mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/author_name_view.xml',
        'data/ir_sequence_book.xml',
        'data/mail_template_view.xml',
        'data/issue_book_action.xml',
        'views/book_details_view.xml',
        'views/register_books_view.xml',
        'views/issue_books_view.xml',
        'views/register_date_view.xml',
        'views/book_type_view.xml',
        'wizard/issue_book_button_view.xml',
        'wizard/return_book_button_view.xml',
        'report/book_report.xml',
        'report/book_report_templates.xml'
        
    ],
    "demo": [],
    "qweb": [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
