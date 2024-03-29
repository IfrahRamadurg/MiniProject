import math

#Squareroot computation
def compute_sqrt(number):
    try:
        return round(math.sqrt(number),2)
    except Exception as e:
        return e

#Factorial Computation
def compute_factorial(number):
    try:
        return round(math.factorial(number),2)
    except Exception as e:
        return e

#Log Computation
def compute_log(number):
    try:
        return round(math.log(number),2)
    except Exception as e:
        return e

#Power Computation
def compute_power(base,power):
    try:
        return round(math.pow(base,power),2)
    except Exception as e:
        return e

#Print result
def print_result(result):
    print("result:{0}".format(result))
