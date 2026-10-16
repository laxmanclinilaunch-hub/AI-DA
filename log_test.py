from log import *


def add(a,b):
    result = a + b
    logging.info(f"Adding {a} and {b}, result: {result}")
    return result

def subtract(a,b):
    result = a - b
    
    return logging.info(f"Subtracting {b} from {a}, result: {result}")


def multiply(a,b):
    result = a * b
    
    return logging.info(f"Multiplying {a} and {b}, result: {result}")  

def divide(a,b):
    if b == 0:
        logging.error("Attempted to divide by zero.")
        raise ValueError("Denominator cannot be zero.")
    result = a / b
    
    return logging.info(f"Dividing {a} by {b}, result: {result}")







add(5,2)

subtract(5,2)

multiply(5,2)

divide(10,2)