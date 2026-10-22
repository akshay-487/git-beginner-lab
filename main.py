def freq_count(user_list):

    result = {}

    for num in user_list:
        if num in result:
            result[num] =+1 
        else:
            result[num] = 1 
    return result

user_list = list(map(int,input("Enter a separetd numbers: ").split()))    
print(freq_count(user_list)) 