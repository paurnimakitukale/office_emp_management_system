from django.http import HttpResponse
class FirstMiddleware(object):
    def __init__(self,get_response):
        print("this is constructor")
        self.get_response = get_response

    def __call__(self,request):    
        return HttpResponse('<h1>This is under Maintainence</h1>')
        return response 