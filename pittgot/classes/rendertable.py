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
  p = q.get()
  usermajor = p.major
  usercourses = p.courses

  # majorCourses = usermajor.lower()
  # majorCourses = majorCourses.replace(" ", "")
  # majorCourses = majorCourses + ".csv"

  # if(majorCourses == ".csv"):
  #   majorCourses = "computerengineering.csv"
      
  #file open
  # with open(majorCourses, 'r') as csvfile:
  #   csvreader = csv.reader(csvfile, dialect='excel')
  #   courseList = list(csvreader)
    
  courseNames = {}
  courseId = {}
  courseCredits = {}
  courseGrades = {}
  tableElement = {}
  userclassestaken = {}
  i = 0
  for course in usercourses:
    userclassestaken[i] = course.courseTaken
    courseNames[i] = course.courseName
    courseId[i] = course.courseId
    courseCredits[i] = course.courseCredits
    courseGrades[i] = course.courseGrade
    i = i+1
            
  #userclassestaken = p.classTaken
  cur_user = p

  count = 0
  for i in range(40):
    if(userclassestaken):
      if(userclassestaken[i] == True):
        tableElement[i] = "#a2edb1"
        count = count = count +1
      else:
        tableElement[i] = "#ffffff"
    else:
      tableElement[i] = "#ffffff"

  cur_user.gradProgress = 100*count/40
  cur_user.put()


  homepage_params = {
 'name' : user.nickname(),
 'courseNames': courseNames,
 'courseId': courseId,
 'courseCredits': courseCredits,
 'courseGrades' : courseGrades,
 'classTaken': tableElement,
 'graduationProgress': cur_user.gradProgress,
 'debug': userclassestaken
  }
  render_template(self, 'main.html', homepage_params)

