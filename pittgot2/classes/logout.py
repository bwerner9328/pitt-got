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

class Logout(webapp2.RequestHandler):
  def get(self):
    self.redirect(users.create_logout_url('/'))