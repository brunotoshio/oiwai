""" Tests for party module
"""

from business import party


class TestCreateParty:
    """ Tests for create party
    """
    def test_success(self, mongo):
        result, errors = party.create_party(mongo, 'Birthday', description='My birthday')

        assert result
        assert errors is None
        assert mongo.parties.count_documents({}) == 1
        saved_party = mongo.parties.find({})[0]
        assert saved_party['description'] == 'My birthday'
        assert saved_party['name'] == 'Birthday'

    def test_missing_name(self, mongo):
        result, errors = party.create_party(mongo, '', '')

        assert not result
        assert len(errors) > 0
        assert 'name is required' in errors
        assert mongo.parties.count_documents({}) == 0
    
    def test_success_with_description(self, mongo):
        result, errors = party.create_party(mongo, 'Birthday', description='My birthday')

        assert result
        assert errors is None
        assert mongo.parties.count_documents({}) == 1
    
    
