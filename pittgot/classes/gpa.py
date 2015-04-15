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
from student import Student
import rendertemplate

render_template = rendertemplate.render_template


class GPA(webapp2.RequestHandler) :
    def get(self) :
      user = users.get_current_user()
      q = Student.query(Student.email == user.email())
      p = q.get()
      cur_user = p

      gpa_params = {
      "name" : user.nickname(),
      "studgpa": cur_user.gpa,
      'graduationProgress': cur_user.gradProgress,
      'credTaken': cur_user.creditsTaken,
      }
      render_template(self, 'gpa.html', gpa_params)
