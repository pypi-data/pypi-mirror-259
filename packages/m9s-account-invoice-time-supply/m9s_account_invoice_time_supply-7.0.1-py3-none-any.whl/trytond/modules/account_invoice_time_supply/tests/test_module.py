# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase


class AccountInvoiceTimeSupplyTestCase(ModuleTestCase):
    "Test Account Invoice Time Supply module"
    module = 'account_invoice_time_supply'


del ModuleTestCase
