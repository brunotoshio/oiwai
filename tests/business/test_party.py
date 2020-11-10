""" Tests for party module
"""

from business import party


class TestCreateParty:
    """ Tests for create party
    """
    def test_success(self, mongo):
        result, errors = party.create_party(mongo, 'Birthday')

        assert result
        assert errors is None
        assert mongo.parties.count_documents({}) == 1

    def test_missing_name(self, mongo):
        result, errors = party.create_party(mongo, '')

        assert not result
        assert len(errors) > 0
        assert 'name is required' in errors
        assert mongo.parties.count_documents({}) == 0
