import random
import string
import json
import time
import re
import vdcd.data_create as dc
import vdcd.server_chaos_monkey
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

cm = vdcd.server_chaos_monkey.ServerMonkey()

def index(request):
  return HttpResponse("Hello World! This is going to be the VDC Dummy ")

def patient(request):
  para_amount = get_parameters_amount(request)
  res = cm.patient(para_amount)
  if(res==False):
    return HttpResponse(status=500)
  return JsonResponse(res)

def exam(request):
  para_amount = get_parameters_amount(request)
  res = cm.exam(para_amount)
  if(res==False):
    return HttpResponse(status=500)
  return JsonResponse(res)

def find(request):
  para_amount = get_parameters_amount(request)
  res = cm.find(para_amount)
  if(res==False):
    return HttpResponse(status=500)
  return JsonResponse(res)

def behaviour(request):
  #Get behaviour from form-data
  no_response = request.POST.get('no_response',None)
  if no_response=="True":
    cm.event.clear()
    no_response= True
  elif no_response=="False":
    cm.event.set()
    no_response==False
  else:
    no_response=cm.no_response
  wait_time = request.POST.get('wait_time',None)
  if wait_time==None:
    wait_time=cm.wait_time
  error_rate = request.POST.get('error_rate',None)
  if error_rate==None:
    error_rate= cm.error_rate
  data_reduction= request.POST.get('data_reduction',None)
  if data_reduction==None:
    data_reduction= cm.data_reduction

  #Get behaviour from Json
  json_data = json.loads(str(request.body)[2:-1])
  if 'no_response' in json_data:
    no_response = json_data['no_response']
    print(no_response)
  if 'data_reduction' in json_data:
    data_reduction = json_data['data_reduction']
  if 'error_rate' in json_data:
    error_rate = json_data['error_rate']
  if 'wait_time' in json_data:
    wait_time = json_data['wait_time']



  cm.parameter(int(wait_time),int(error_rate),no_response,int(data_reduction))
  return HttpResponse("No Response: "+str(cm.no_response)+ "\nWait Time:  "+ str(cm.wait_time)+ "\nError Rate:  "+ str(cm.error_rate) +" \nData Reduction:  "+ str(cm.data_reduction),content_type="text/plain")

def get_parameters_amount(request):
  patient_id= request.GET.getlist("patientid")
  patient_ssn= request.GET.getlist("ssn")
  exam_try= request.GET.getlist("try")
  exam_chol= request.GET.getlist("chol")
  exam_hep= request.GET.getlist("hep")
  date= request.GET.getlist("date")
  return len(patient_id)+len(patient_ssn)+len(exam_try)+len(exam_hep)+len(exam_chol)+len(date)