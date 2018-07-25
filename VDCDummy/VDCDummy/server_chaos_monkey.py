from django.conf import settings
from django.http import HttpResponse
from time import sleep
from random import randint
import threading
import VDCDummy.data_create as dc

'''
The ServerMonkey is a class to simulate failures of the VDC you can tinker with latency, 
randomly throw errors, make the server unresponsive or give back significantly less data
'''
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


    def parameter(self,new_wt, new_er,new_nr, new_ld):
        self.wait_time = new_wt
        self.error_rate = new_er
        self.no_response = new_nr
        self.data_reduction = new_ld

    #applies the set error parameters to every request
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
        size = (1000/(para_amount+1))/(self.data_reduction+1)
        return dc.create_patient_list(size)


    def exam(self,para_amount):
        error = self.latency_and_errors()
        if error == False:
            return error
        size = (3000/(para_amount+1))/(self.data_reduction+1)
        return dc.create_exam_list(size=size)

    def find(self,para_amount):
        error = self.latency_and_errors()
        if error == False:
            return error
        size = (3000/(para_amount+1))/(self.data_reduction+1)
        return dc.create_exam_list(size=size * 3)