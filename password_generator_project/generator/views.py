from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Must return a HTTP response
def home(req):
    # Plain text is not the best option
    # return HttpResponse('Hello there friend')
    return render(req,'generator/home.html')

def about(req):
    return render(req,'generator/about.html')

# Necessary for random password generation
import random
# All letters
import string

def password(req):
    characters = list(string.ascii_lowercase)
    result_password= ''
    # Get password options from request
    # 12 is default returned value
    length = int(req.GET.get('length',12))
    
    # Check if uppercase option is checked
    if req.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    
    # Check if special characters option is checked
    if req.GET.get('special'):
        characters.extend(list('!@#$%^&**()_+|\\[];:.,/?`~{\}'))

    # Check if special characters option is checked
    if req.GET.get('numbers'):
        characters.extend(list('1234567890'))    
    

    for x in range(length):
        result_password+=random.choice(characters)

    return render(req,'generator/password.html',{'password':result_password})
