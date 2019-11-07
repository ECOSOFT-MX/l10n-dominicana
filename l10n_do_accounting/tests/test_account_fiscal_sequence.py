

from odoo.tests.common import TransactionCase


class AccountFiscalSequenceTests(TransactionCase):

    """
    The following tests are executed in a post-install context.
    This means that all fiscal sequence demo data are pre-loaded
    and are considered as existing data as every tests cursor
    is instantiated.
    """

    def setUp(self):
        super(AccountFiscalSequenceTests, self).setUp()

        self.fiscal_sequence_obj = self.env['account.fiscal.sequence']
        self.credito_fiscal = self.ref(
            'l10n_do_accounting.fiscal_type_credito_fiscal')

    def test_001_fiscal_sequence_queue(self):
        """
        Validates only one sequence per type can be queue
        """

        sequence_id = self.fiscal_sequence_obj.create({
            'name': '7045195031',
            'fiscal_type_id': self.credito_fiscal,
            'sequence_start': 300,
            'sequence_end': 310,
        })

        # Because there is one demo credito fiscal sequence queued,
        # sequence can_be_queue must be False
        self.assertEqual(sequence_id.can_be_queue, False)

# Account Fiscal Sequence Tests

# TODO: warning_gap is correctly computed
# TODO: sequence_remaining is correctly computed
# TODO: next_fiscal_number is correctly computed
# TODO: default sequence_start is correctly computed
# TODO: unique active sequence ValidationError raised
# TODO: _validate_sequence_range() ValidationErrors raised
# TODO: internal sequence is deleted when fiscal sequence is deleted
# TODO: fiscal sequence is auto expired if expiration_date is today
# TODO: when a draft fiscal sequence is confirmed, a internal sequence
#  is created too with correct vals
# TODO: when a draft fiscal sequence is confirmed, a new internal sequence
#  is attached and state == 'active'
# TODO: when a fiscal sequence is cancelled, its internal sequence is set to
#  inactive and state == 'cancelled'
# TODO: a fiscal sequence is auto-depleted when its get out of available
#  sequences
# TODO: a fiscal sequence of random type always returns the correct combination
#  of prefix-padding-sequence string
