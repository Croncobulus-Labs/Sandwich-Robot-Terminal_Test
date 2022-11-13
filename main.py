import requests
import sys

URLBASE = ""

def make_sandwich():
    response = requests.get(URLBASE + "/open")
    if response.status_code != 200:
        return "open request failed"
    
    response = requests.get(URLBASE + "/squeeze")
    if response.status_code != 200:
        return "squeeze request failed"

    response = requests.get(URLBASE + "/close")
    if response.status_code != 200:
        return "close request failed"

    return("Done Making Sandwich")

def refill():
    response = requests.get(URLBASE + "/refill")
    if response.status_code != 200:
        return "refill request failed"

    response = requests.get(URLBASE + "/open")
    if response.status_code != 200:
        return "open request failed"

    return("Refill Open")

def done_refill():
    response = requests.get(URLBASE + "/close")
    if response.status_code != 200:
        return "close request failed"

    return("Done Refill")

if __name__ == '__main__':
    if sys.arv[1] == 'make':
        print(make_sandwich())
    elif sys.arv[1] == 'refill':
        print(refill())
    elif sys.argv[1] == 'done':
        print(done_refill())
    