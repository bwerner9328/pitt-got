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



class Main(webapp2.RequestHandler):
  def get(self) :
    usermajor = "computerengineering"
    userclassestaken = {}

    user = users.get_current_user()
    q = Student.all()
    q.filter("email =", user.email())
    if user:
      for p in q.run(limit=1):
        usermajor = p.major
        userclassestaken = p.classTaken
        cur_user = p
      
      majorCourses = usermajor.lower()
      majorCourses = majorCourses.replace(" ", "")
      majorCourses = majorCourses + ".csv"

      if(majorCourses == ".csv"):
        majorCourses = "computerengineering.csv"
      
      #file open
      with open(majorCourses, 'r') as csvfile:
        csvreader = csv.reader(csvfile, dialect='excel')
        courseList = list(csvreader)
    
      courseNames = {}
      courseCredits = {}
      courseId = {}
      tableElement = {}

      i = 0
      for row in courseList:
        courseNames[i] = row[0]
        courseId[i] = row[1]
        courseCredits[i] = row[2]
        i = i+1


      count = 0
      for i in range(40):
        if(userclassestaken):
          if(userclassestaken[i] == True):
            tableElement[i+1] = "bgcolor=#00FF00"
            count = count = count +1
          else:
            tableElement[i+1] = "bgcolor=#FFF"
        else:
          tableElement[i+1] = "bgcolor=#FFF"

      p.gradProgress = 100*count/40
      p.put()

      homepage_params = {
      'name' : user.nickname(),
      'courseNames': courseNames,
      'courseCredits': courseCredits,
      'courseId': courseId,
      'classTaken': tableElement,
      'graduationProgress': p.gradProgress,
      'debug': userclassestaken
      }
      render_template(self, 'main.html', homepage_params)
    else:
      self.redirect(users.create_login_url(self.request.uri))


  def post(self) :
    user = users.get_current_user()
    with open("computerengineering.csv", 'r') as csvfile:
      csvreader = csv.reader(csvfile, dialect='excel')
      courseList = list(csvreader)
      courseNames = {}

    courseCredits = {}
    courseId = {}
    tableElement = {}
    addCourse = self.request.get('courseCompleted')
    i = 0
    for row in courseList:
      courseNames[i] = row[0]
      if courseNames[i] == addCourse :
        courses_taken = db.GqlQuery("SELECT * FROM Student WHERE email = :email", email=user.email())
        for e in courses_taken:
          if(len(e.classTaken) != 40):
            e.classTaken = [False]*40
          e.classTaken[i-1] = True
          db.put(e)
      i = i+1
    courses_params = {
    'graduationProgress' : 0
    }
    render_template(self, 'main.html', courses_params)

