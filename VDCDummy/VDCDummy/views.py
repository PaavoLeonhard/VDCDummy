import random
import string
import json
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import VDCDummy.data_create as dc
import VDCDummy.server_chaos_monkey as server_chaos_monkey

cm = server_chaos_monkey.ServerMonkey()

#returns a list of up to 1000 patients, depending on the amount of parameters given
def patient(request):
  para_amount = get_parameters_amount(request)
  res = cm.patient(para_amount)
  if(res==False):
    return HttpResponse(status=500)
  return JsonResponse(res)

#returns a list of exam up to 3000
def exam(request):
  para_amount = get_parameters_amount(request)
  res = cm.exam(para_amount)
  if(res==False):
    return HttpResponse(status=500)
  return JsonResponse(res)

#returns a list of exams up to 9000
def find(request):
  para_amount = get_parameters_amount(request)
  res = cm.find(para_amount)
  if(res==False):
    return HttpResponse(status=500)
  return JsonResponse(res)

#interface to change the behavior of the server to accomadate for different types and amount of errors
@csrf_exempt
def behaviour(request):
  #Get behaviour from form-data
  request_body = request.body
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
  try:
    json_data = json.loads(str(request_body)[2:-1])
    if 'no_response' in json_data:
      no_response = json_data['no_response']
    if 'data_reduction' in json_data:
      data_reduction = json_data['data_reduction']
    if 'error_rate' in json_data:
      error_rate = json_data['error_rate']
    if 'wait_time' in json_data:
      wait_time = json_data['wait_time']
  except:
    pass
  cm.parameter(int(wait_time),int(error_rate),no_response,int(data_reduction))
  return HttpResponse("No Response: "+str(cm.no_response)+ "\nWait Time:  "+ str(cm.wait_time)+ "\nError Rate:  "+ str(cm.error_rate) +" \nData Reduction:  "+ str(cm.data_reduction),content_type="text/plain")

#counts the amount of parameters given to scale down the size of the returned lists
def get_parameters_amount(request):
  patient_id= request.GET.getlist("patientid")
  patient_ssn= request.GET.getlist("ssn")
  exam_try= request.GET.getlist("try")
  exam_chol= request.GET.getlist("chol")
  exam_hep= request.GET.getlist("hep")
  date= request.GET.getlist("date")
  return len(patient_id)+len(patient_ssn)+len(exam_try)+len(exam_hep)+len(exam_chol)+len(date)