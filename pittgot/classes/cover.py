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
import rendertable

render_template = rendertemplate.render_template
render_table = rendertable.render_table
#The first page they come to. cover page
class Cover(webapp2.RequestHandler):
  def get(self) :
    user = users.get_current_user()
    if user:
      q = Student.all()
      q.filter("email =", user.email())
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
    falseBoolList = [False] * 40
    regUser = Student(email = user.email(), major = self.request.get('Major'), classTaken = falseBoolList, gpa = float(self.request.get('GPA')), creditsTaken = int(self.request.get('creditsTaken')))
    regUser.put()
    main_params = {
      "name" : user.nickname()
    }
    render_template(self, 'main.html', main_params)