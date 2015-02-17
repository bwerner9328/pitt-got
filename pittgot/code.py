import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template


userclassestaken = {}
graduationProgress = 0

def render_template(handler, templatename, templatevalues) :
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)

#The data storage for user info
class Users(db.Model) :
  email = db.StringProperty(required=True)
  major = db.StringProperty(required=True)
  classTaken = db.ListProperty(bool)
  gpa = db.FloatProperty()
  creditsTaken = db.IntegerProperty()
  
#The first page they come to. Log in page.
class MainPage(webapp2.RequestHandler):

    def get(self):
      user = users.get_current_user()
      if user:
        q = Users.all()
        q.filter("email =", user.email())
        if q.get(): #checks if email is in database.
          main_params = {
          "name" : user.nickname()
          }
          render_template(self, 'main.html', main_params)
        else :
          welcome_params = {
          "name" : user.nickname()
          }
          render_template(self, 'welcome.html', welcome_params)

      else:
        self.redirect(users.create_login_url(self.request.uri))

    def post(self):
      user = users.get_current_user()
      falseBoolList = [False] * 40
      regUser = Users(email = user.email(), major = self.request.get('Major'), classTaken = falseBoolList, gpa = float(self.request.get('GPA')), creditsTaken = int(self.request.get('creditsTaken')))
      regUser.put()
      main_params = {
        "name" : user.nickname()
      }
      render_template(self, 'main.html', main_params)
    
class Settings(webapp2.RequestHandler) :
    def get(self) :
      user = users.get_current_user()
      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': graduationProgress
      }
      render_template(self, 'settings.html', settings_params)

class Courses(webapp2.RequestHandler) :
    def get(self):
      user = users.get_current_user()
      q = Users.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
      majorCourses = usermajor.lower()
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
      }
      render_template(self, 'courses.html', courses_params)

class CourseSelect(webapp2.RequestHandler) :
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
          courses_taken = db.GqlQuery("SELECT * FROM Users WHERE email = :email", email=user.email())
          for e in courses_taken:
            e.classTaken[i-1] = True
            db.put(e)
        i = i+1

      courses_params = {

      }
      render_template(self, 'courseSelect.html', courses_params)

class Homepage(webapp2.RequestHandler) :
    def get(self):
      user = users.get_current_user()
      q = Users.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
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
      for i in range(40):
        q = Users.all()
        q.filter("email =", user.email())
        for p in q.run(limit=1):
          userclassestaken = p.classTaken
        if(userclassestaken):
          if(userclassestaken[i] == True):
            tableElement[i+1] = "bgcolor=#00FF00"
          else:
            tableElement[i+1] = "bgcolor=#FF0000"
        else:
          tableElement[i+1] = "bgcolor=#FF0000"
      homepage_params = {
      'name' : user.nickname(),
      'courseNames': courseNames,
      'courseCredits': courseCredits,
      'courseId': courseId,
      'classTaken': tableElement,
      'graduationProgress': graduationProgress
      }
      render_template(self, 'homepage.html', homepage_params)

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/settings', Settings),
  ('/courses', Courses),
  ('/homepage', Homepage),
  ('/CourseSelect', CourseSelect),
])
