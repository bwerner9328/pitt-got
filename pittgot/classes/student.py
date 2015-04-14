import cgi
import cgitb
import os
import csv
import webapp2
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template
import rendertemplate

render_template = rendertemplate.render_template
#The data storage for student info
class Student(db.Model) :
  email = db.StringProperty(required=True)
  major = db.StringProperty(required=True)
  classTaken = db.ListProperty(bool)
  gpa = db.FloatProperty()
  creditsTaken = db.IntegerProperty()
  gradProgress = db.IntegerProperty()
  classTakenGrade = db.ListProperty(str)
  avatar = db.BlobProperty()
  #  modified student db elements for courses
  courseNames = db.ListProperty(str)
  coursesTaken = db.ListProperty(bool)
  courseCredits = db.ListProperty(int)
  courseGrades = db.ListProperty(str)
  # db elements for calendar events
  eventTitle = db.ListProperty(str)
  eventAllDay = db.ListProperty(bool)
  eventID = db.ListProperty(int)
  eventStart = db.ListProperty(datetime.time)
  eventEnd = db.ListProperty(datetime.time)
