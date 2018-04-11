# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import json
from models.user import User


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')


class GetUsers(webapp2.RequestHandler):
  def get(self):
    name = self.request.get('name')
    results = []
    if name:
      results = User.query(User.name == name).fetch()
    else:
      results = User.query().fetch()

    output = {'users': [r.to_dict() for r in results]}
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json.dumps(output, encoding='utf8'))


class AddUser(webapp2.RequestHandler):
  def get(self):
    name = self.request.get('name')
    email = self.request.get('email')
    user = User()
    if name and email:
      user = User(name=name, email=email)
      user.put()

    output = {'user': user.to_dict()}
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json.dumps(output, encoding='utf8'))


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/user/create', AddUser),
  ('/users', GetUsers)
], debug=True)
