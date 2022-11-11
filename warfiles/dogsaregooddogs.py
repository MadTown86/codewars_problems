"""

#Top Answers:

#1:
import re

def we_rate_dogs(s, rating):
    return re.sub(r"\d+\/\d+", f"{rating}/10", s)

#2
import re

def we_rate_dogs(stg, rating):
    return re.sub(r"\d+/", f"{rating}/", stg)

#3
def we_rate_dogs(string, rating):
    l = string.find("/")
    return string[0:l-1] + "{}/10".format(rating) + string[l+3:]
"""