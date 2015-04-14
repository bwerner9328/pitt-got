import cgi
import cgitb
import os
import csv
import webapp2
import datetime
import re
import logging
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from student import Student
from student import Events
import rendertemplate

render_template = rendertemplate.render_template

class ScheduleDelete(webapp2.RequestHandler) :
    def post(self):
      req = self.request.arguments().pop()
      
      user = users.get_current_user()
      q = Student.query(Student.email == user.email())
      p = q.get()
      
      events = p.events
      logging.info(int(req))
      for i in xrange(len(p.events) -1, -1, -1):
        if p.events[i].eventID==int(req):
          del p.events[i]


      # event name
      

      p.put()