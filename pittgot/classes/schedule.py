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
import rendertemplate

render_template = rendertemplate.render_template




class Schedule(webapp2.RequestHandler) :
    def get(self) :
      user = users.get_current_user()
      q = Student.query(Student.email == user.email())
      p = q.get()
      usermajor = p.major
      events = p.events

      i = 0;
      events_string = "events: ["

      for e in events:
        if i == 0:
          events_string = events_string +"{"
          i=i+1
        else:
          events_string = events_string +",{"
        events_string = events_string +"id: " +e.eventID+","
        events_string = events_string +"title: '"+e.eventTitle+"',"
        if e.eventAllDay:
          events_string = events_string +"start: '"+ e.eventStart[:10]+"'"
        else:
          events_string = events_string +"start: '"+ e.eventStart+"'"
          events_string = events_string +"start: '"+ e.eventEnd+"'"
        events_string = events_string + "}"


      events_string = events_string + "]"
      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")

      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': 70,
      'events': events_string,
      'date': date,
      }
      render_template(self, 'agenda-views.html', settings_params)
    def post(self):
      req = self.request.arguments().pop()
      allreq = req.split(",")
      user = users.get_current_user()
      q = Student.all()
      q.filter("email =", user.email())
      for p in q.run(limit=1):
        usermajor = p.major
        events = p.Events
        i = 0;
        curid = len(eventID)+1
        # event name
        if(len(allreq[0]) > 0 & len(allreq[0] < 30)):
          # repeat
          if(allreq[2] is on):
            if(allreq[3] is not None):
              # allday
              while i < int(allreq[3]):
                if(allreq[1] is on):
                  new_event = Events(eventTitle=allreq[0], eventAllDay=True, eventID=curid, eventStart=allreq[4]+"-"+allreq[5]+"-"+allreq[6]+"T"+allreq[7], eventEnd=allreq[8]+","+allreq[9]+","+allreq[10]+","+allreq[11])
                else:
                  new_event = Events(eventTitle=allreq[0], eventAllDay=True, eventID=curid, eventStart=allreq[4]+"-"+allreq[5]+"-"+allreq[6]+"T"+allreq[7], eventEnd=allreq[8]+","+allreq[9]+","+allreq[10]+","+allreq[11])
                
                events.append(new_event)

        p.Events = events
        cur_user = p
        db.put(p)


