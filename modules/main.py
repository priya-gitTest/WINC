# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this #Zen of python
import time
import math
import datetime
import sys
import greet

def wait(seconds):
    time.sleep(seconds)
    return 
print(wait(0.8))

def my_sin(float_num):
    return math.sin(float_num)

def iso_now():
    #return  datetime.datetime.now().isoformat()
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    
print(iso_now())
def platform():
    return sys.platform

def supergreeting_wrapper(name):
    return greet.supergreeting(name)
    
print(supergreeting_wrapper('aa'))#Hellooo...ooo, aa!