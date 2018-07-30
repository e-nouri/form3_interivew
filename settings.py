import yaml

with open("./models/payment_v0.yaml", "r") as f:
    schema = yaml.load(f.read())

# Let's just use the local mongod instance. Edit as needed.
# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'form3'

payments = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's'
    'item_title': 'payment',
    'allow_unknown': True,
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': schema
}


# Enable reads (GET), inserts (POST)
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']
# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
# ALLOWED_FILTERS = ['*']
# VALIDATE_FILTERS = True
ID_FIELD = 'id'
ITEM_LOOKUP_FIELD = 'id'
ITEM_URL = 'regex("[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}")'
IF_MATCH = False
ITEMS = 'data'
DOMAIN = {'payments': payments}
