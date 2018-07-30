import re
from cerberus import Validator
 
class ValidatorUuid(Validator):
    def _validate_is_uuid(self, is_uuid, field, value):
        re_uuid = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', re.I)
        if is_uuid and not re_uuid.match(value):
            self._error("Value for field '%s' must be valid UUID" % field)
