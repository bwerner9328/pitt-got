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
#The data storage for student info
class Student(db.Model) :
  email = db.StringProperty(required=True)
  major = db.StringProperty(required=True)
  classTaken = db.ListProperty(bool)
  gpa = db.FloatProperty()
  creditsTaken = db.IntegerProperty()
  gradProgress = db.IntegerProperty()
  classTakenGrade = db.ListProperty(str)