from odoo import api, SUPERUSER_ID
from . import models


def bank_information_sync(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.bank'].bank_information_sync()