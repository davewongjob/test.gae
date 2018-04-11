from google.appengine.ext import ndb

# Ref: https://docs.google.com/document/d/1F4Gy3NUdYGbCHrGzyoRDsGaElSNtn3bPJ1VTciWriS0/edit
class User(ndb.Model):
  name = ndb.StringProperty()
  email = ndb.StringProperty()
