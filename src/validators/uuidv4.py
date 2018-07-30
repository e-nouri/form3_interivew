from eve.io.mongo import Validator
from uuid import UUID

class UUIDValidator(Validator):
    """
    Extends the base mongo validator adding support for the uuid data-type
    """
    def _validate_type_uuid(self, value):
        try:
            UUID(value)
            return True

        except ValueError:
            return False