
def calculator(int1,int2,task):
    task = task.lower() 

    if task =="add":
        return int1+int2 

    elif task=="sub":
        return int1 - int2 

    elif task =="mul":
        return int1 * int2 

    elif task =="div":
        if int2 ==0:
            return "cannot divide by zero" 
        return int1/int2 
    else:
        return "invalid input" 


print(calculator(1,2,"add"))


    


    



