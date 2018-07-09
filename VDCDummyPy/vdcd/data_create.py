from django.conf import settings
from django.http import HttpResponse
from time import sleep
from random import randint
import random
import string


def create_patient():
    def func():
        pass
    func.ssn=random.randint(100000,999999)
    func.last_name=(str(random.choice(string.ascii_uppercase))+ ''.join(random.choice(string.ascii_lowercase) for _ in range(12)))
    func.name = (str(random.choice(string.ascii_uppercase))+ ''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
    func.gender = random.choice(["male", "female", "undefined"])
    func.email = func.name + func.last_name + str(random.choice(["@googlemail.com","@yahoo.nz","@ise.de","@gmx.net","@reddit.com","@isengart.me","@web.de","@outlook.com","@feuerbart.io"])) 
    func.birthday = random.choice(["3.6.2018:23.34.34","3.8.2016:34.34.34","7.6.2015:24.54.34","3.4.2018:4.23.12","3.6.2018:13.34.56"])
    #func.exams = create_exam_list(func.ssn,func.last_name,func.name)
    return func.__dict__

def create_exam(ssn=51423, last_name="Grey", name="Dorian"):
  def func():
    pass
  func.ssn = ssn
  func.last_name = last_name
  func.name = name
  func.date = random.choice(["3.6.2018:23.34.34","3.8.2016:34.34.34","7.6.2015:24.54.34","3.4.2018:4.23.12","3.6.2018:13.34.56"])# some random Date
  func.cholesterol = random.randint(1,3000)/345.3456
  func.triglyceride = random.randint(1,11000)/345.3456
  func.hepatitis = random.choice([True, False])
  return func.__dict__

def create_patient_list(size=18):
  def func():
    pass
  patients = []
  for i in range(1, int(size)):
    patients.append(create_patient())
  func.patients=patients
  return func.__dict__



def create_exam_list(ssn=51423, last_name="Grey", name ="Dorian", size = 25):
  def func():
    pass
  exams = []
  for i in range(1, int(size)):
    exams.append(create_exam(ssn,last_name,name))
  func.exams=exams
  return func.__dict__

