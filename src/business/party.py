""" Party module

    This module handles all logic for managing parties
"""

def create_party(name):
    """ Create a party

        Args:
            name: the name of the party
        Returns:
            True in case of success, False otherwise.
            An list of errors if the operation failed.
    """
    if not name:
        return False, ['name is required']
    return True, None
