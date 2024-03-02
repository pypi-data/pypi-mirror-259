# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'

    _states = {
        'readonly': Eval('state') != 'draft',
    }

    time_of_supply_start = fields.Date('Time of Supply Start', states=_states)
    time_of_supply_end = fields.Date('Time of Supply End', states=_states)

    del _states

    def _credit(self, **values):
        credit = super()._credit()
        credit.time_of_supply_start = self.time_of_supply_start
        credit.time_of_supply_end = self.time_of_supply_end
        return credit
