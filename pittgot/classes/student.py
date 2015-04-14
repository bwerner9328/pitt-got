import cgi
import cgitb
import os
import csv
import webapp2
import datetime
import urllib
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template
import rendertemplate

render_template = rendertemplate.render_template
class Events(ndb.Model):
  eventTitle = ndb.StringProperty()
  eventAllDay = ndb.BooleanProperty
  eventID = ndb.IntegerProperty()
  eventStart = ndb.StringProperty()
  eventEnd = ndb.StringProperty()
class Course(ndb.Model):
  courseTaken = ndb.BooleanProperty()
  courseName = ndb.StringProperty()
  courseId = ndb.StringProperty()
  courseCredits = ndb.IntegerProperty()
  courseGrade = ndb.StringProperty()
#The data storage for student info
class Student(ndb.Model) :
  email = ndb.StringProperty()
  major = ndb.StringProperty()
  classTaken = ndb.BooleanProperty(repeated=True)
  gpa = ndb.FloatProperty()
  creditsTaken = ndb.IntegerProperty()
  gradProgress = ndb.IntegerProperty()
  classTakenGrade = ndb.StringProperty(repeated=True)
  # db elements for calendar events
  events = ndb.StructuredProperty(Events, repeated=True)
  courses = ndb.StructuredProperty(Course, repeated=True)


