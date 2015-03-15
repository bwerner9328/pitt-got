import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
import rendertemplate

render_template = rendertemplate.render_template

class Login(webapp2.RequestHandler):
  def get(self) :
    user = users.get_current_user()
    if user:
      login_params = {
      "name" : user.nickname()
      }
      render_template(self, 'main.html', login_params)
    else:
      self.redirect(users.create_login_url(self.request.uri))

  def post(self):
    user = users.get_current_user()
    falseBoolList = [False] * 40
    regUser = Users(email = user.email(), major = self.request.get('Major'), classTaken = falseBoolList, gpa = float(self.request.get('GPA')), creditsTaken = int(self.request.get('creditsTaken')))
    regUser.put()
    main_params = {
      "name" : user.nickname()
    }
    render_template(self, 'welcome.html', main_params)