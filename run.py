import os
from eve import Eve
from src.validators.uuidv4 import UUIDValidator
from src.encoders.encoder import Encoder
from eve_auth_jwt import JWTAuth


# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

app = Eve(
    auth=JWTAuth,
    json_encoder=Encoder,
    validator=UUIDValidator)


if __name__ == '__main__':
    app.run(host=host, port=port)