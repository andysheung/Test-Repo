import sys
import requests
from os import rename
import math

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = 'Test'
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("http://google.com")
print(r.status_code)
