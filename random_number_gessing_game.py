import random

ges = input("ges a number 1 tho 100 ")
type(ges)
r = random.randint(1, 100)

def valid_ges(num):
    while True:
        try:
            num = int(num)
            if (num == r):
                break
            elif num > 100:
                print("try a number below 100")
                num = input("pic a number 1 tho 100 ")
            elif(num <= 100):
                print("your "+str(r - num)+" away")
                num = input("pic a number 1 tho 100 ")
        except:
            print("Ooops error plz try one more time")
            num = input("pic a number 1 tho 100 ")
     
valid_ges(ges)

print("yay you did it")


