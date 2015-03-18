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

class StoreImg(webapp2.RequestHandler) :
    def post(self) :
      user = users.get_current_user()
      q = Student.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
        cur_user = p

      # Get image data
      avatar = self.request.get('img')
      # Transform the image
      #avatar = images.resize(avatar, 32, 32)
      p.avatar = avatar

      p.put()

      return self.redirect("/settings")
