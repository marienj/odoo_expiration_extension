# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from dateutil.relativedelta import relativedelta

import logging
import datetime
from datetime import date
from odoo import api, fields, models, tools, _


class Licence(models.Model):
    
    _name = 'licence.extension'
    _description = 'Licence Extension'

    date = fields.Date('Expiration date', required=True)


    def extend(self):
        self.ensure_one()
        date = self.date
        print("Extension date choosed: %s" % date)
        extension_date = "%s 00:00:00" % date
        self.env.cr.execute("UPDATE ir_config_parameter SET value = '%s' WHERE key='database.expiration_date'" % extension_date)
        #update ir_config_parameter set value = '2024-12-20 11:50:46' where key='database.expiration_date';
