from package import circle,square,triangle
from log import *

# print("circlearea",circle.area(5))


# print("circle circumference",circle.circumference(5))



# print("squre area",square.area(5))

# print("square perimeter",square.perimeter(5))



# print("triangle area",triangle.area(5,10)) 
# print("triangle perimter",triangle.perimeter(3,4,5))


logging.info(f"circlearea {circle.area(5)}")


logging.info(f"circle circumference ,{circle.circumference(5)}")



logging.info(f"squre area:  {square.area(5)}")

logging.info(f"square perimeter {square.perimeter(5)}")



logging.info(f"triangle area {triangle.area(5,10)}") 
logging.info(f"triangle perimter {triangle.perimeter(3,4,5)}")