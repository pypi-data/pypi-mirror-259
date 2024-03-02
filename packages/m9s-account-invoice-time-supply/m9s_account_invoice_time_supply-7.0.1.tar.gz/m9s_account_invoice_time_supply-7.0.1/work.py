# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import ModelView


class Work(metaclass=PoolMeta):
    __name__ = 'project.work'

    @classmethod
    @ModelView.button
    def invoice(cls, works):
        pool = Pool()
        Work = pool.get('project.work')

        super().invoice(works)
        works_ids = [w.id for w in works]
        works = Work.search([
                ('parent', 'child_of', works_ids),
                ])
        invoice_ids = set()
        for work in works:
            if work.invoice_line and work.invoice_line.invoice:
                invoice_ids.add(work.invoice_line.invoice.id)
            for twork in work.timesheet_works:
                for timesheet_line in twork.timesheet_lines:
                    if (timesheet_line.invoice_line
                            and timesheet_line.invoice_line.invoice):
                        invoice_ids.add(timesheet_line.invoice_line.invoice.id)
            if work.invoiced_progress:
                for progress in work.invoiced_progress:
                    invoice_ids.add(progress.invoice_line.invoice.id)
        cls.postprocess_invoices(invoice_ids)

    @classmethod
    def postprocess_invoices(cls, invoice_ids):
        pool = Pool()
        TimeSheetLine = pool.get('timesheet.line')
        Invoice = pool.get('account.invoice')
        Date = pool.get('ir.date')

        today = Date.today()
        invoices = Invoice.browse(invoice_ids)
        for invoice in [i for i in invoices if i.state == 'draft']:
            time_of_supply_start = today
            time_of_supply_end = None
            timesheet_lines = TimeSheetLine.search([
                ('invoice_line', 'in', [l.id for l in invoice.lines]),
                ])
            for line in timesheet_lines:
                if line.date < time_of_supply_start:
                    time_of_supply_start = line.date
                if time_of_supply_end is None:
                    time_of_supply_end = time_of_supply_start
                elif line.date > time_of_supply_end:
                    time_of_supply_end = line.date
            invoice.time_of_supply_start = time_of_supply_start
            invoice.time_of_supply_end = time_of_supply_end
            invoice.save()
