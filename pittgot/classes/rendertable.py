import cgi
import cgitb
import os
import csv
import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from classes.student import Student
import rendertemplate

render_template = rendertemplate.render_template

def render_table(self, q):
	user = users.get_current_user()
	for p in q.run(limit=1):
          usermajor = p.major

        majorCourses = usermajor.lower()
        majorCourses = majorCourses.replace(" ", "")
        majorCourses = majorCourses + ".csv"

        if(majorCourses == ".csv"):
          majorCourses = "computerengineering.csv"
      
        #file open
        with open(majorCourses, 'r') as csvfile:
          csvreader = csv.reader(csvfile, dialect='excel')
          courseList = list(csvreader)
    
        courseNames = {}
        courseCredits = {}
        courseId = {}
        tableElement = {}

        i = 0
        for row in courseList:
          courseNames[i] = row[0]
          courseId[i] = row[1]
          courseCredits[i] = row[2]
          i = i+1
          
        q = Student.all()
        q.filter("email =", user.email())
        for p in q.run(limit=1):
          userclassestaken = p.classTaken
          cur_user = p

        count = 0
        for i in range(40):
          if(userclassestaken):
            if(userclassestaken[i] == True):
              tableElement[i+1] = "#a2edb1"
              count = count = count +1
            else:
              tableElement[i+1] = "#ffffff"
          else:
            tableElement[i+1] = "#ffffff"

        cur_user.gradProgress = 100*count/40
        cur_user.put()


        homepage_params = {
        'name' : user.nickname(),
        'courseNames': courseNames,
        'courseCredits': courseCredits,
        'courseId': courseId,
        'classTaken': tableElement,
        'graduationProgress': cur_user.gradProgress,
        'debug': userclassestaken
        }
        render_template(self, 'main.html', homepage_params)

