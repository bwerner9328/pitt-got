import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from login import Login
from logout import Logout
from cover import Cover
from settings import Settings

app = webapp2.WSGIApplication([
  ('/', Cover),
  ('/main', Login),
  ('/logout', Logout),
  ('/settings', Settings)
])

