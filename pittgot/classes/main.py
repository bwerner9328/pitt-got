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
from classes.student import Course
import rendertemplate
import rendertable
import logging

import json


render_template = rendertemplate.render_template
render_table = rendertable.render_table
global q

class Main(webapp2.RequestHandler):
  def get(self) :
    usermajor = "computerengineering"
    userclassestaken = {}
    courseNames = {}
    courseCredits = {}
    courseId = {}
    tableElement = {}

    user = users.get_current_user()
    if(user):
      q = Student.query(Student.email == user.email())
      if q.get():
        render_table(self, q)



      else:
        welcome_params = {
        "name" : user.nickname()
        }
        render_template(self, 'welcome.html', welcome_params)
    else:
      self.redirect(users.create_login_url(self.request.uri))


  def post(self) :
    user = users.get_current_user()
      
    q = Student.query(Student.email == user.email())
    
    #TODO Store them into db!
    cellnumber = int(self.request.get('cellnumber'))
    courseTaken = bool(self.request.get('coursetaken'))
    courseName = str(self.request.get('coursename'))
    courseId = str(self.request.get('courseid'))
    courseCredits = int(self.request.get('credits'))
    courseGrade = str(self.request.get('grade'))

    if q.get():
      p = q.get()
      p.courses[cellnumber].courseTaken = courseTaken      
      p.courses[cellnumber].courseName= courseName
      p.courses[cellnumber].courseId = courseId      
      p.courses[cellnumber].courseCredits= courseCredits
      p.courses[cellnumber].courseGrade = courseGrade
      p.put()
      render_table(self, q)

    # with open("computerengineering.csv", 'r') as csvfile:
    #   csvreader = csv.reader(csvfile, dialect='excel')
    #   courseList = list(csvreader)
    #   courseNames = {}

    # courseCredits = {}
    # courseId = {}
    # tableElement = {}    
    # # addCourse = self.request.get('courseCompleted')
    # temp = self.request.arguments().pop()
    # addCourses = temp.split("|")
    # # logging.info("temp is %s", temp)

    # for addCourse in addCourses:      
    #   i = 0
    #   for row in courseList:
    #     courseNames[i] = row[0]
    #     #logging.info("courseNames[i] is %s", courseNames[i])
    #     if courseNames[i] == addCourse :
    #       courses_taken = db.GqlQuery("SELECT * FROM Student WHERE email = :email", email=user.email())
    #       for e in courses_taken:
    #         if(len(e.classTaken) != 40):
    #           e.classTaken = [False]*40
    #         if e.classTaken[i-1] == False:
    #           e.classTaken[i-1] = True
    #         else:
    #           e.classTaken[i-1] = False
    #         logging.info("on or off: %r", e.classTaken[i-1]) 
    #         db.put(e)
    #     i = i+1
    #   courses_taken = db.GqlQuery("SELECT * FROM Student WHERE email = :email", email=user.email())
    #   for e in courses_taken:
    #     logging.info("class is taken: %r", e.classTaken[1])
    
