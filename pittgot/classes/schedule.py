import cgi
import cgitb
import os
import csv
import webapp2
import datetime
import re
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from student import Student
import rendertemplate

render_template = rendertemplate.render_template




class Schedule(webapp2.RequestHandler) :
    def get(self) :
      user = users.get_current_user()
      q = Student.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
        cur_user = p

      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")
      events_string = """events: [
        {
          title: \'All Day Event\',
          start: '2015-03-01'
        },
        {
          title: 'Long Event',
          start: '2015-03-07',
          end: '2015-03-10'
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: '2015-03-09T16:00:00'
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: '2015-03-16T16:00:00'
        },
        {
          title: 'Conference',
          start: '2015-03-11',
          end: '2015-03-13'
        },
        {
          title: 'Meeting',
          start: '2015-03-12T10:30:00',
          end: '2015-03-12T12:30:00'
        },
        {
          title: 'Lunch',
          start: '2015-03-12T12:00:00'
        },
        {
          title: 'Meeting',
          start: '2015-03-12T14:30:00'
        },
        {
          title: 'Happy Hour',
          start: '2015-03-12T17:30:00'
        },
        {
          title: 'Dinner',
          start: '2015-03-12T20:00:00'
        },
        {
          title: 'Birthday Party',
          start: '2015-03-13T07:00:00'
        },
        {
          title: 'Click for Google',
          url: 'http://google.com/',
          start: '2015-03-28'
        }
      ]"""

      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': 70,
      'events': events_string,
      'date': date
      }
      render_template(self, 'agenda-views.html', settings_params)
    def post(self):
      user = users.get_current_user()
      q = Student.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
        cur_user = p

      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")
      events_string = """events: [
        {
          title: \'All Day Event\',
          start: '2015-03-01'
        },
        {
          title: 'Long Event',
          start: '2015-03-07',
          end: '2015-03-10'
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: '2015-03-09T16:00:00'
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: '2015-03-16T16:00:00'
        },
        {
          title: 'Conference',
          start: '2015-03-11',
          end: '2015-03-13'
        },
        {
          title: 'Meeting',
          start: '2015-03-12T10:30:00',
          end: '2015-03-12T12:30:00'
        },
        {
          title: 'Lunch',
          start: '2015-03-12T12:00:00'
        },
        {
          title: 'Meeting',
          start: '2015-03-12T14:30:00'
        },
        {
          title: 'Happy Hour',
          start: '2015-03-12T17:30:00'
        },
        {
          title: 'Dinner',
          start: '2015-03-12T20:00:00'
        },
        {
          title: 'Birthday Party',
          start: '2015-03-13T07:00:00'
        },
        {
          title: 'Click for Google',
          url: 'http://google.com/',
          start: '2015-03-28'
        }
      ]"""

      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': 70,
      'events': events_string,
      'date': date
      }
      render_template(self, 'agenda-views.html', settings_params)