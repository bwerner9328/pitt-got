import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from student import Student
import rendertemplate

render_template = rendertemplate.render_template


class Settings(webapp2.RequestHandler) :
    def get(self) :
      user = users.get_current_user()
      q = Student.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
        cur_user = p

      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': 70
      }
      render_template(self, 'settings.html', settings_params)

    def post(self) :
      user = users.get_current_user()
      falseBoolList = [False] * 40
      regUser = Student(email = user.email(), major = self.request.get('Major'), classTaken = falseBoolList, gpa = float(self.request.get('GPA')), creditsTaken = int(self.request.get('creditsTaken')))
      regUser.put()
      main_params = {
        "name" : user.nickname()
      }
      render_template(self, '.html', main_params)