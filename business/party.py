""" Party module

    This module handles all logic for managing parties
"""


def create_party(db, name):
    """ Create a party

        Args:
            db: the database connection
            name: the name of the party
        Returns:
            True in case of success, False otherwise.
            An list of errors if the operation failed.
    """
    if not name:
        return False, ['name is required']
    party = {
        'name': name
    }
    db.parties.insert_one(party)
    return True, None
