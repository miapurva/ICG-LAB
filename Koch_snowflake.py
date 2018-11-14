#Submission by Yutika Kulwe, CED15I017
#Koch Snowflake
from turtle import *

def snowflake(lengthSide, level): 
    if level == 0: 
        forward(lengthSide) 
        return
    lengthSide= lengthSide/3.0
    snowflake(lengthSide, level-1) 
    left(60) 
    snowflake(lengthSide, level-1) 
    right(120) 
    snowflake(lengthSide, level-1) 
    left(60) 
    snowflake(lengthSide, level-1) 
  
# main function 
if __name__ == "__main__": 
    #speed of the turtle 
    speed(-0.5)

    length = 300.0       
    penup()                      
    backward(length/2.0)   
    pendown()            
    for i in range(3):     
        snowflake(length, 4) 
        right(120) 
    mainloop()