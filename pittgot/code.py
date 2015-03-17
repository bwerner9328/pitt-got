import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from classes.main import Main
from classes.logout import Logout
from classes.cover import Cover
from classes.settings import Settings
from classes.courses import Courses
from classes.profile import Profile
from classes.contact import Contact
from classes.schedule import Schedule

app = webapp2.WSGIApplication([
  ('/', Cover),
  ('/main', Main),
  ('/logout', Logout),
  ('/settings', Settings),
  ('/courses', Courses),
  ('/profile', Profile),
  ('/contact', Contact),
  ('/schedule', Schedule),
])

