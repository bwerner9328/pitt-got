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
        events_string = events_string +"id: " +str(e.eventID)+","
        events_string = events_string +"title: '"+e.eventTitle+"',"
        if e.eventAllDay:
          events_string = events_string +"start: '"+ e.eventStart[:10]+"'"
        else:
          events_string = events_string +"start: '"+ e.eventStart+"',"
          events_string = events_string +"end: '"+ e.eventEnd+"'"
        events_string = events_string + "}"


      events_string = events_string + "]"
      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")
      eventList = []
      idList = []
      for e in events:
        if e.eventID not in idList:
          eventList.append(e.eventTitle +" (id: " + str(e.eventID)+")")
          idList.append(e.eventID)


      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': 70,
      'events': events_string,
      'date': date,
      'eventList': eventList
      }
      render_template(self, 'agenda-views.html', settings_params)

    def post(self):
      req = self.request.arguments().pop()
      allreq = req.split(",")
      user = users.get_current_user()
      q = Student.query(Student.email == user.email())
      p = q.get()
      
      usermajor = p.major
      events = p.events
      i = 0;
      if p.curid is None:
        p.curid = 0
        curid = 0
      else:
        curid = p.curid+1
        p.curid = p.curid+1
      # event name
      
      if(len(allreq[0]) > 0 & len(allreq[0]) < 30):
        # repeat
        if(allreq[2] == "true"):
          if(allreq[3] is not None):
            # allday
            while i < int(allreq[3]):
              if(allreq[1] is "true"):
                new_event = Events(eventTitle=allreq[0], eventAllDay=True, eventID=curid, eventStart=allreq[4]+"-"+allreq[5]+"-"+str((int(allreq[6])+i*7))+"T"+allreq[7]+":00:00", eventEnd=allreq[8]+"-"+allreq[9]+"-"+allreq[10]+"T"+allreq[11]+":00:00")
              else:
                new_event = Events(eventTitle=allreq[0], eventAllDay=False, eventID=curid, eventStart=allreq[4]+"-"+allreq[5]+"-"+str((int(allreq[6])+i*7))+"T"+allreq[7]+":00:00", eventEnd=allreq[8]+"-"+allreq[9]+"-"+allreq[10]+"T"+allreq[11]+":00:00")
              
              p.events.append(new_event)
              i=i+1
      p.put()

      i = 0;
      events_string = "events: ["
      events = p.events
      for e in events:
        if i == 0:
          events_string = events_string +"{"
          i=i+1
        else:
          events_string = events_string +",{"
        events_string = events_string +"id: " +str(e.eventID)+","
        events_string = events_string +"title: '"+e.eventTitle+"',"
        if e.eventAllDay:
          events_string = events_string +"start: '"+ e.eventStart[:10]+"'"
        else:
          events_string = events_string +"start: '"+ e.eventStart+"',"
          events_string = events_string +"end: '"+ e.eventEnd+"'"
        events_string = events_string + "}"


      events_string = events_string + "]"
      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")
      eventList = []
      idList = []
      for e in events:
        if e.eventID not in idList:
          eventList.append(e.eventTitle +" (id: " + str(e.eventID)+")")
          idList.append(e.eventID)


      settings_params = {
      "name" : user.nickname(),
      'graduationProgress': 70,
      'events': events_string,
      'date': date,
      'eventList': eventList
      }
      render_template(self, 'agenda-views.html', settings_params)


