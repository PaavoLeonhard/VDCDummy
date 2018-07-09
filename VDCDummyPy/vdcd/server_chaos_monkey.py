from django.conf import settings
from django.http import HttpResponse
from time import sleep
from random import randint
import threading
import vdcd.data_create as dc


class ServerMonkey():
    wait_time = 0
    error_rate = 0
    no_response = False
    data_reduction = 0
    event = threading.Event()
    
    def __init__(self):
        self.wait_time = 0
        self.respond_error = False
        self.error_rate = 0
        self.event = threading.Event()
        self.no_response = False
        self.less_data = 0
    def testing(self):
        return "Just testing init" 
    def parameter(self,new_wt, new_er,new_nr, new_ld):
        self.wait_time = new_wt
        self.error_rate = new_er
        self.no_response = new_nr
        self.data_reduction = new_ld

    def latency_and_errors(self):
        #Server is not responding
        if self.no_response == True:
            self.event.wait()
        #Server has a higher latency
        sleep(self.wait_time)
        #Server throws Server Errors
        if int(self.error_rate) !=0:
            errorTrigger = randint(0,100)
            print(errorTrigger)
            if errorTrigger < int(self.error_rate):
                return False
        #Server returns less data
        return True

    def patient(self,para_amount):
        error = self.latency_and_errors()
        if error == False:
            return error
        #result = []
        #for x in range(0,para_amount +2):
        #    result.append(dc.create_patient())
        size = (1000/(para_amount+1))/(self.data_reduction+1)
        return dc.create_patient_list(size)

    def exam(self,para_amount):
        error = self.latency_and_errors()
        if error != False:
            return error
        #result = []
        #for x in range(0,para_amount +2):
        #    result.append(dc.create_patient())
        size = (3000/(para_amount+1))/(self.data_reduction+1)
        return dc.create_exam_list(size=size)

    def find(self,para_amount):
        error = self.latency_and_errors()
        if error == False:
            return error
        #result = []
        #for x in range(0,para_amount +2):
        #    result.append(dc.create_patient())
        size = (3000/(para_amount+1))/(self.data_reduction+1)
        return dc.create_exam_list(size=size * 3)

    
'''
    def exam(para_amount):
        error = latency_and_errors()
        if error != False:
            return error
        return dc.create_exam_list()

    def find(para_amount):
        error = latency_and_errors()
        if error != False:
            return error
        return dc.find()
'''