import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
import rendertemplate

render_template = rendertemplate.render_template
#The first page they come to. cover page
class Cover(webapp2.RequestHandler):
  def get(self) :
    cover_params = {}
    render_template(self, 'coverpage.html', cover_params)