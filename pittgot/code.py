import cgi
import cgitb
import os
import csv
import webapp2
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template
from classes.main import Main
from classes.logout import Logout
from classes.cover import Cover
from classes.settings import Settings
from classes.courses import Courses
from classes.gpa import GPA
from classes.contact import Contact
from classes.schedule import Schedule
from classes.storeimg import StoreImg
from classes.scheduleDelete import ScheduleDelete

app = webapp2.WSGIApplication([
  ('/', Cover),
  ('/main', Main),
  ('/logout', Logout),
  ('/settings', Settings),
  ('/courses', Courses),
  ('/gpa', GPA),
  ('/contact', Contact),
  ('/sign', StoreImg),
  ('/schedule', Schedule),
  ('/scheduleDelete', ScheduleDelete)
])
