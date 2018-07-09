from django.conf import settings
from django.http import HttpResponse
from time import sleep
from random import randint
import threading

class NoReturnMiddleware: 
    def __init__(self, get_response):
        self.get_response= get_response
        self.parameter = parameter()
        pass

    def __call__(self, request):
        response = self.get_response(request)
        parameter.no_response = bool(request.GET.get('no_response',parameter.no_response))
        parameter.wait_time =  int(request.GET.get('wait_time',parameter.wait_time))
        parameter.respond_error = bool(request.GET.get('respond_error',parameter.respond_error))
        parameter.error_rate = float(request.GET.get('error_rate',parameter.error_rate))

        #Server is not responding
        if parameter.no_response == True:
            parameter.event.wait()
        #Server has a higher latency
        sleep(parameter.wait_time)
        #Server throws Server Errors
        if parameter.respond_error == True:
            errorTrigger = randint(0,10) * parameter.error_rate
            if errorTrigger > 50:
                return HttpResponse(status=500)
        #Server returns less data
        return response



class parameter():
    wait_time = 0
    respond_error = False
    error_rate = 0
    no_response = False
    event = threading.Event()
    def __init__(self):
        self.wait_time = 0
        self.respond_error = False
        self.error_rate = 0
        self.event = threading.Event()
        self.no_response = False

    def func():
        print("I am a function YAAY")