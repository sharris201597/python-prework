#question 1

def hello_name(user_name):
    print("Hello " + user_name)

#question 2

def first_odds() :
    for num in range(100):
        if num % 2 == 1:
            print(num)
    num += 1

#question 3

def max_num_in_list(a_list):
    return max(a_list)

#question 4

def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif a_year % 400 == 0:
        return True
    else: 
        return False 

#question 5

def is_consecutive(a_list):
     for i in range(0, len(a_list)-1):
        if (a_list[i] + 1 == a_list[i+1]) or (a_list[i] - 1 == a_list[i + 1]):
             return True
        else:
            return False
            break

