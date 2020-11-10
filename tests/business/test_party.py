""" Tests for party module
"""

from business import party


class TestCreateParty:
    """ Tests for create party
    """
    def test_success(self):
        result, errors = party.create_party('Birthday')

        assert result
        assert errors is None

    def test_missing_name(self):
        result, errors = party.create_party('')

        assert not result
        assert len(errors) > 0
        assert 'name is required' in errors
