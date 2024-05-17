from . import models


def bank_information_sync(env):
    env['res.bank'].bank_information_sync()
