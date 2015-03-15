import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from classes.login import Login
from classes.logout import Logout
from classes.cover import Cover
from classes.settings import Settings
from classes.courses import Courses
from classes.profile import Profile

app = webapp2.WSGIApplication([
  ('/', Cover),
  ('/main', Login),
  ('/logout', Logout),
  ('/settings', Settings),
  ('/courses', Courses),
  ('/profile', Profile)
])

