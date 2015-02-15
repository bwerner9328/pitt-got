import cgi
import cgitb
import os
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template

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
  
#The first page they come to. Log in page.
class LogIn(webapp2.RequestHandler) :
  def get(self) :
    template_params = {
    
    }
    render_template(self, 'index.html', template_params)
	
#Page they get on if they are already registered and logged in.
class MainPage(webapp2.RequestHandler) :
  def post(self) :
    q = Users.all()
    q.filter("email =", self.request.get('emaillogin'))
    if q.get(): #checks if username is in database.
    	q.filter("password =", self.request.get('passwordlogin'))
    	if q.get(): #checks if password is in database.
			for p in q.run (limit=1):
				name = p.name
				email = p.email
				password = p.password
				major = p.major
			main_params = {
			"name" : name
			}
			render_template(self, 'mainpage-v2.html', main_params)
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
    m.filter("email =", self.request.get('emailregister'))
    if not m.get(): #if email not registered yet.
    	if not self.request.get('nameregister') or not self.request.get('emailregister') or not self.request.get('passwordregister') :
    		message = "Cannot have blank fields in your registration."
    		template_params = {
			"registered" : message,
			}
    		render_template(self, 'index.html', template_params)
    	else :
			user = Users(name = self.request.get('nameregister'), email = self.request.get('emailregister'), password = self.request.get('passwordregister'), major = self.request.get('Major'))
			user.put()
			welcome_params = {
			"name" : user.name
			}
			render_template(self, 'mainpage-v2.html', welcome_params)
    else : #if email already registered.
    	message = "That email has already been registered."
    	template_params = {
    	"registered" : message,
    	}
    	render_template(self, 'index.html', template_params)
		
class Settings(webapp2.RequestHandler) :
    def get(self) :
      self.response.write("Hello")

class Courses(webapp2.RequestHandler) :
    def get(self):
      self.response.write("Blah")
	  
app = webapp2.WSGIApplication([
  ('/', LogIn),
  ('/home', MainPage),
  ('/welcome', Welcome),
  ('/settings', Settings),
  ('/courses', Courses),
])