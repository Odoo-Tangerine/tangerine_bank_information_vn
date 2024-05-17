from . import models
from odoo import api, SUPERUSER_ID


def bank_information_sync(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.bank'].bank_information_sync()
