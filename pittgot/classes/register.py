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
import rendertable

render_template = rendertemplate.render_template
render_table = rendertable.render_table

class Register(webapp2.RequestHandler) :
  def post(self) :
    user = users.get_current_user()
    falseBoolList = [False] * 40
    q = Student.query(Student.email == user.email())
    p = q.get()
    p.major = self.request.get('Major')
    p.put()
    render_table(self, q)
    return self.redirect("/")
