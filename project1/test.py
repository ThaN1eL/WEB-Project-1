#import math

#x = int(math.sqrt(9))

#print(x)

#x = 5
#y = -3

#print(pow(x,y))
#print(abs(y))


#recursion   
"""
1= 1
2= 2+1
3= 3+3
4= 4+6
5= 5+10
6= 6+15
7= 7+21
"""
def walk(steps):
    if steps == 1:
        return 1
    else:
        return steps + walk(steps-1)
    
result= walk(7)
print(result)


#iterative
#def walk(steps):
    #for step in range(steps):
        #print(step)

#walk(106)