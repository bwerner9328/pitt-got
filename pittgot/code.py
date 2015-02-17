import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template

username = ""
useremail = ""
usermajor = ""
userclassestaken = {}
graduationProgress = 0

def render_template(handler, templatename, templatevalues) :
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)

#The data storage for user info
class Users(db.Model) :
  name = db.StringProperty(required=True)
  email = db.StringProperty(required=True)
  password = db.StringProperty(required=True)
  major = db.StringProperty(required=True)
  classTaken = db.ListProperty(bool)
  gpa = db.FloatProperty(required=True)
  creditsTaken = db.IntegerProperty(required=True)
  
#The first page they come to. Log in page.
class LogIn(webapp2.RequestHandler) :
  def get(self) :
    if username == "" :
      template_params = {
      
      }
      render_template(self, 'index.html', template_params)
    else :
      main_params = {
        "name" : username
        }
      render_template(self, 'main.html', main_params)
  
#Page they get on if they are already registered and logged in.
class MainPage(webapp2.RequestHandler) :
  def post(self) :
    q = Users.all()
    q.filter("email =", self.request.get('emaillogin'))
    if q.get(): #checks if username is in database.
      q.filter("password =", self.request.get('passwordlogin'))
      if q.get(): #checks if password is in database.
        for p in q.run (limit=1):
          global username
          global useremail
          global usermajor
          global userclassestaken
          global creditsTaken
          global graduationProgress
          username = p.name
          useremail = p.email
          password = p.password
          usermajor = p.major
          userclassestaken = p.classTaken
          creditsTaken = 70
          graduationProgress = creditsTaken/127
        main_params = {
        "name" : username
        }
        render_template(self, 'main.html', main_params)
      else : #if password incorrect.
        message = "Incorrect Log In Information."
        template_params = {
        "incorrectLogin" : message
        }
        render_template(self, 'index.html', template_params)
    else : #if username is incorrect.
      message = "Incorrect Log In Information."
      template_params = {
      "incorrectLogin" : message,
      }
      render_template(self, 'index.html', template_params)

class Welcome(webapp2.RequestHandler) :
  def post(self) :
    m = Users.all()
    falseBoolList = [False] * 40
    m.filter("email =", self.request.get('emailregister'))
    if not m.get(): #if email not registered yet.
      if not self.request.get('nameregister') or not self.request.get('emailregister') or not self.request.get('passwordregister') :
        message = "Cannot have blank fields in your registration."
        template_params = {
        "registered" : message,
        }
        render_template(self, 'index.html', template_params)
      else :
        user = Users(name = self.request.get('nameregister'), email = self.request.get('emailregister'), password = self.request.get('passwordregister'), major = self.request.get('Major'), classTaken = falseBoolList, gpa = 0.0, creditsTaken = 0 )
        user.put()
        global username
        global useremail
        global usermajor
        global userclassestaken
        global graduationProgress
        username = user.name
        useremail = user.email
        usermajor = user.major
        userclassestaken = user.classTaken
        graduationProgress = 0
        welcome_params = {
        "name" : username,
        'graduationProgress': graduationProgress
        }
        render_template(self, 'welcome.html', welcome_params)
    else : #if email already registered.
      message = "That email has already been registered."
      template_params = {
      "registered" : message,
      'graduationProgress': graduationProgress
      }
      render_template(self, 'index.html', template_params)
    
class Settings(webapp2.RequestHandler) :
    def get(self) :
      settings_params = {
      "name" : username,
      'graduationProgress': graduationProgress
      }
      render_template(self, 'settings.html', settings_params)
<<<<<<< HEAD

=======
class CourseSelect(webapp2.RequestHandler) :
    def post(self) :
      classTaken[self.request.get('courseCompleted')] = true
      courses_params = {

      }
      render_template(self, 'courseSelect.html', courses_params)
>>>>>>> origin/bens_branch
class Courses(webapp2.RequestHandler) :
    def get(self):
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
<<<<<<< HEAD
      "name" : username,
      'graduationProgress': graduationProgress
=======
      'name' : username,
      'courseNames': courseNames,
      'classTaken': tableElement,
>>>>>>> origin/bens_branch
      }
      render_template(self, 'courses.html', courses_params)

class Homepage(webapp2.RequestHandler) :
    def get(self):
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
        if(userclassestaken):
          if(userclassestaken[i] == True):
            tableElement[i+1] = "bgcolor=#00FF00"
          else:
            tableElement[i+1] = "bgcolor=#FF0000"
        else:
          tableElement[i+1] = "bgcolor=#FF0000"
      homepage_params = {
      'name' : username,
      'courseNames': courseNames,
      'courseCredits': courseCredits,
      'courseId': courseId,
      'classTaken': tableElement,
      'graduationProgress': graduationProgress
      }
      render_template(self, 'homepage.html', homepage_params)

app = webapp2.WSGIApplication([
  ('/', LogIn),
  ('/home', MainPage),
  ('/welcome', Welcome),
  ('/settings', Settings),
  ('/courses', Courses),
<<<<<<< HEAD
  ('/homepage', Homepage),
])
=======
  ('/courseSelect', CourseSelect),
  ('/homepage', Homepage)
])
>>>>>>> origin/bens_branch
