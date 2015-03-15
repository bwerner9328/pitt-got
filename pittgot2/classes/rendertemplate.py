import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues) :
  path = os.path.join(os.path.dirname(__file__), '../templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)
