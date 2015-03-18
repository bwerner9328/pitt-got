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


class Profile(webapp2.RequestHandler) :
    def get(self) :
      user = users.get_current_user()
      q = Student.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
        cur_user = p
      
      if p.avatar:
        self.response.headers['Content-Type'] = 'image/png'
        self.response.out.write(p.avatar)
      else:
        self.response.out.write('No image')

      profile_params = {
      "name" : user.nickname(),
      'graduationProgress': cur_user.gradProgress,
      }
      render_template(self, 'profilepic.html', profile_params)
