import math
import os
import random
import re
import sys
# Complete the 'timeInWords' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
def timeInWords(h, m):
    # Write your code here
    def word(dy):
        days = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eigth', 'nine', 'ten', 'eleven', 'tweleve', 'thirteen', 'fourteen', 'fivteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        day = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty']
        if(dy < 20):
            return days[dy]
        return day[dy/10] + ' ' + days[dy%10]       
    def manu(dy):
        w = word(dy)
        if(dy == 1):
            return w + ' minute'
        else:
            return w + ' minutes'        
    if(m == 0):
        return "{} o' clock".format(word(h))
    elif(m == 15):
        return "quarter past {}".format(word(h))
    elif(m == 30):
        return "half past {}".format(word(h))
    elif(m == 45):
        return "quarter to {}".format(word(h+1))
    elif(m < 30):
        return "{} past {}".format(manu(m), word(h))
    else:
        return "{} to {}".format(manu(60-m), word(h+1))      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    fptr.write(result + '\n')
    fptr.close()