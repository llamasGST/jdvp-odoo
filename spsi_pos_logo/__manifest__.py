# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'SPSI POS Logo',
    'version': '12.0.1.0.0',
    'summary': """Logo For Every Point of Sale (Screen & Receipt)""",
    'description': """"This module helps you to set a logo for every point of sale. This will help you to
                 identify the point of sale easily. You can also see this logo in pos screen and pos receipt.
                 (receipt includes point-of-sale header & footer)""",
    'category': 'Point Of Sale',
    'author': 'SPSI Sistemas',
    'company': 'SPSI Sistemas',
    # 'website': "http://www.cybrosys.com",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/pos_config_image_view.xml',
        'views/pos_image_view.xml',
    ],
    'qweb': ['static/src/xml/pos_ticket_view.xml',
             'static/src/xml/pos_screen_image_view.xml'],
    'images': ['static/description/Logo-256.png'],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
