

def q1(): 
    word = str(input("Input a word: "))
    if (word[-2:]) == "ey":
        print("eys")
    
    elif (word[-1]) == "y":
        print("ies")
    
    elif (word[-3:]) == "ife":
        print("ives")
    
    else: 
        print("s")



def q2(): 
    num =  int(input("Input a number :"))
    if num > 0:
        print("num is positive")

    elif num < 0:
        print("num is negative")


def q3():
    num =  int(input("Input a number :"))
    morenum =  int(input("Input another number :"))
    evenmorenum =  int(input("Input a third number :"))

    if num + morenum <= evenmorenum:
        print("No Triangle")

    elif num == morenum == evenmorenum:
        print("Equilateral")

    elif num == morenum:
        print("Isosceles")

    else:
        print("Scalene")



#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
