""" Party module

    This module handles all logic for managing parties
"""


def create_party(db, name, description):
    """ Create a party

        Args:
            db: the database connection
            name: the name of the party
            description: the description of the party
        Returns:
            True in case of success, False otherwise.
            An list of errors if the operation failed.
    """
    errors = []
    if not name:
        errors.append('name is required')
    if not description:
        errors.append('description is required')
    if errors:
        return False, errors
    party = {
        'name': name,
        'description': description
    }
    db.parties.insert_one(party)
    return True, None
