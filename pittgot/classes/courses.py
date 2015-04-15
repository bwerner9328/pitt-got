import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from classes.student import Student
import rendertemplate

render_template = rendertemplate.render_template

class Courses(webapp2.RequestHandler) :
    def get(self):
      user = users.get_current_user()
      q = Student.query(Student.email == user.email())
      p = q.get()
      
      #file open
      with open("computerengineering.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile, dialect='excel')

        courseList = list(csvreader)
 
        courseNames = {}
        courseCredits = {}
        courseId = {}
        tableElement = {}

      i = 0
      for row in courseList:
        courseNames[i] = row[0]
        i = i+1
          
      courses_params = {
      'name' : user.nickname(),
      'courseNames': courseNames,
      'classTaken': tableElement,
      'graduationProgress': 70
      }
      render_template(self, 'courses.html', courses_params)