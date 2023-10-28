from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Must return a HTTP response
def home(req):
    # Plain text is not the best option
    # return HttpResponse('Hello there friend')
    return render(req,'generator/home.html')

def test_page(req):
    return render(req,'generator/test_page.html',{'test_message':'test'})
