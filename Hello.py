


# print("Hello world")
a = 2

# print(a)
# en_st= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+ "
# print (en_st[len(en_st)-10::]
def is_palindrome(): 
    a = input("check if palindrome")
    a = a.lower()
    a = a.replace(" ", "")
    b = a[::-1]

    if a == b:
        print ("ok")
    else:
        print ("not")

def temperature_convert():  
    a = input("insert the temperature you would like to convert")
    a = a.lower()
    if a[len(a)-1] == "f":
        a = a.replace("f", "")
        converted = (int(a) *5 -160) /9
        print(round(converted), "c")
    elif a[len(a)-1] == "c":
        a = a.replace("c", "")
        converted = (int(a) *9 + (32*5))/5
        print(round(converted), "f")

def date_weekday():#gets date and returns weekday/
    import calendar
    
    a = input("insert date here:")

    date = []
    date.append(a[:2:])
    date.append(a[3:5:])
    date.append(a[6::])
    date[0] = int(date[0])
    date[1] = int(date[1])
    date[2] = int(date[2])
    # print (date)
    a = calendar.weekday(date[2],date[1],date[0])
    # print(a)

    if a == 6:
        print("sunday")
    elif a == 0:
        print("monday")
    elif a == 1:
        print("tuesday")
    elif a == 2:
        print("wednesday")
    elif a == 3:
        print("thursday")
    elif a == 4:
        print("friday")
    elif a == 5:
        print("saturday")

date_weekday()
def is_early(str):#checks if the last sign in string is earlier un the string.
    str = str.lower()
    a = str[len(str)-1]
    if str.find(a) < len(str)-1:
        print ("True")
    else:
        print ("False")

def distance(num1, num2, num3):#idiot practice
    if (num2 -num1 == 1 or num3 -num1 == 1) and num3 -num2 > 1:
        print ("True")
    elif (num2 -num1 == 1 or num3 -num1 == 1) and num2 -num3 > 1:
        print ("True")
    else:
        print("False")

def fix(num):#same
    if num == 13 or num == 14 or num == 17 or num == 18 or num == 19:
        num = 0
    return num
def filter_ages(a =13, b =13 , c =13):#same
    a = fix(a)
    b = fix(b)
    c = fix(c)
    print (a+b+c)

def could_row(s,b,l):#checks if i couls make a row length l, out of parameters s*1 and b*5..
    if b *5 +a < l:
        print("impossible")
    elif  l %5 <s:
        print("impossible")
    else:
        print("possilble")

    
import time
T = time.time()
T = round(T)
et = T % 78 #encryption time

#this is a function that using non fixed offset to encrypt messages.
def encrypt(msg):# srting to encrypt, start offset value.
    en_st= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+ ',." #encrypting string
    en_msg = ""
    ev = et + 2 # this is a offset value, evalueated from encryption time, and more one variable to avoid caesar breaking. 
    for letter in msg:
        if  letter in en_st:
            position = en_st.find(letter)#find the msg letter in en_st.
            new_pos = (position + ev) %78
        #fix a offaet.
            new_letter = en_st[new_pos] #the letter after encrypt.
            en_msg = en_msg + new_letter #add the letter to the encrypted message.
        

        else:
            return "letter doesn't supported"
        
        ev = ev + 2

    Te = 4 #time encryption value.
    for letter in str(T):
        position = en_st.find(letter)#find the msg letter in en_st.
        new_pos = (position + 25 + Te) %78
    #fix a offaet.
        new_letter = en_st[new_pos] #the letter after encrypt.
        en_msg = en_msg + new_letter #add the letter to the encrypted message.
        Te = Te + 4
    return en_msg

# print(encrypt(input("enter text for encrypt:"))) 

def s_3(a,b,c):
    [a,b,c] = [b,c,a]
    return [a,b,c]

def extend_list(x,y):
    for i in y:
        x.append(i)
    return x
    

def are_lists_equal(x,y): #checks if lists are equal, even not in order.
    for i in x:
        if not i in y:
            return False
    for i in y:
        if not i in x:
            return False
    else:
        return True
            
def longest_str(x): #returns the longest value in list.
    x.sort(key=len)
    return x[len(x)-1]


# x = ["as","sadfd","a","arscs","aqwsderfgt","fsdfs","as"]
# y = [3,2]
# print (longest_str(x))

def square_numbers(start, stop): #prints the square of each number between start and stop
    start = int(start)
    stop = int(stop)
    while start <= stop:
        print (start **2)
        start = start +1

def is_greater(lst, num): #returns the number in lst that bigger than num.
    """empty list
    loop, checks the corrent ekement in lst:
    if bigger than num: add to gn
    returnung gn"""
    gn = []
    for i in lst:
        if i > num:
            gn.append(i)
    return gn

def num_let_count(str): #returns the number of numbers and the number of other signs.
    count = [0, 0]
    for i in str:
        if i in "0123456789":
            count[0] += 1
        else:
            count[1] += 1
    return count

def seven_boom(end): #return the numbers from 0 to end, no 7 aloowed.
    op = []
    for i in range(0,end+1):
        s = str(i)
        if i % 7 == 0 or "7" in s:
            op.append("boom")
        else:
            op.append(i)
    return op
    
def sequence_del(str): #returs str without sequences.
    s = ""
    for i in range(2,len(str)):
        if str[i] != str[i-1]:
            s += str[i]
    return s

def shopping_list_actions(str): #תרגיל 7.2.6
    x = input("choose action:")
    if x == 1:
        print(str)
    elif x == 2:
        print (str.count(",")+1)
    elif x == 3:
        product = input("enter the item you want to check:")
        if product in str:
            print("yes, ", product, " in the shopping list")
        else:
            print("item not found")
    elif x == 4:
        cnt = (input("enter the item you want to count:"))
        print ("the item is", str.count(cnt)," times in the shopiing list")
    
def arrow(x,ln): #print arrow of x in max length ln.
    x += " "
    for i in range(ln+1):
        print(x*i)
    for i in range(ln-1,0,-1):
        print(x*i)
print(arrow("j",12))
# data = ("self", "py", 1.543)
# format_string = "Hello %s %s learner, you have only %1.1f units left before you master the course!"

# print(format_string % data)
    
def sortPrices(listOfTuples):
    listOfTuples = sorted(listOfTuples, key = lambda tup:tup[1])
    return listOfTuples

# print (sortPrices(([("apple", 3.5),("banana", 2.1),("watermelon", 3.3),("cucomber", 1.9)])))

dict = {}
dict["first_name"] = "miriam"
dict["last_name"] = "carey"
dict["birth_date"] = "27.03.90"
dict["hobbies"] = ["sing", "compose", "act"]
# print (dict["hobbies"])
def dictPractice(dict):
    choice = input("please choose number from one to seven:")

    if choice == "1":
        print(dict["last_name"])
    if choice == "2":
        print(dict["birth_date"][3:5:])
    if choice == "3":
        print(len(dict["hobbies"]))
    if choice == "4":
        print(dict["hobbies"][len(dict["hobbies"])-1])
    if choice == "5":
        dict["hobbies"] += "cooking"

def count_chars1(str):
    dict = {}
    for char in range(len(str)):
        dict[char+1] = str[char]
    return dict

def count_chars2(str):
    dict = {}
    chars = ""
    for char in str:
        if not char in chars:
            dict[char] = str.count(char)
            chars += char
    return dict

# def inverse_dict(dict):
#     reverse_dict = {}
#     cnt = 0
#     keys_list = dict.keys()
#     values_list = dict.values()
#     for i in dict:
#         reverse_dict[cnt] = keys_list[cnt]
#         cnt += 1
#     reverse_dict = sorted(reverse_dict)
#     return reverse_dict
# print (inverse_dict(dict))






# def main():
#     is_palindrome()
#     is_early()
#     fix()
#     filter_ages()
#     could_row()
#     encrypt()
# if __name__ == "__main__":
#     main()