import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail
import rendertemplate

render_template = rendertemplate.render_template

class Contact(webapp2.RequestHandler) :
  def get(self) :
    user = users.get_current_user()
    contact_params = {
        'name' : user.nickname(),
        'email' : user.email(),
        'sent' : False,
    }
    render_template(self, 'contact.html', contact_params)

  def post(self) :
    user = users.get_current_user()
    subj = self.request.get("subject")
    emailbody = self.request.get("emailmessage")
    message = mail.EmailMessage(sender=user.email(),
                            subject=subj)

    message.to = "pittgot.com Support <calenderplannerproject@gmail.com>"
    message.body = emailbody
    message.send()
    contact_params = {
        'name' : user.nickname(),
        'email' : user.email(),
        'sent' : True,
    }
    render_template(self, 'contact.html', contact_params)