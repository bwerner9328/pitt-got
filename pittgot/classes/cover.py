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
from classes.student import Course

import rendertemplate
import rendertable

render_template = rendertemplate.render_template
render_table = rendertable.render_table
#The first page they come to. cover page
class Cover(webapp2.RequestHandler):
  def get(self) :
    user = users.get_current_user()
    if user:
      q = Student.query(Student.email == user.email())
      if q.get(): #checks if email is in database.
        render_table(self, q)
      else :
        welcome_params = {
        "name" : user.nickname()
        }
        render_template(self, 'welcome.html', welcome_params)
    else:
      cover_params = {}
      render_template(self, 'coverpage.html', cover_params)

  def post(self):
    user = users.get_current_user()

    usermajor = self.request.get('Major')
    majorCourses = usermajor.lower()
    majorCourses = majorCourses.replace(" ", "")
    majorCourses = majorCourses + ".csv"

    if(majorCourses == ".csv"):
      majorCourses = "computerengineering.csv"
        
    usercourses =[]
    falseBoolList = [False] * 40      
    #file open
    #      open(majorCourses, 'rU'), dialect=csv.excel_tab
    # with open(majorCourses, 'r') as csvfile:
    #   csvreader = csv.reader(csvfile, dialect='excel')
    with open(majorCourses, 'rU') as csvfile:
      csvreader = csv.reader(csvfile, dialect='excel')
      courseList = list(csvreader)      
      i = -1
      for row in courseList:   
        if (i == -1):
          i = i+1
        else:
          tempCourse = Course(courseTaken=False, courseName=row[0], courseId=row[1], courseCredits=int(row[2]), courseGrade="Did not Take")
          usercourses.append(tempCourse)
          i = i+1
    
    regUser = Student(email = user.email(), major = usermajor, classTaken = falseBoolList, courses = usercourses)
    regUser.put()

    user = users.get_current_user()
    if(user):
      q = Student.query(Student.email == user.email())
      if q.get():
        render_table(self, q)
    main_params = {
    "name" : user.nickname()
    }
    render_template(self, 'main.html', main_params)
