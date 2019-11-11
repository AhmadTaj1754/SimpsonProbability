#! /usr/bin/env python3



import sys
import math


def prob_simpson():

    global probability
    probability = 0

    in1  = sys.argv[1]
    in2 = sys.argv[2]

    lamb    = int(in1)
    x       = int(in2)



    def prob(lamb=lamb, x=x):
        simps = (pow(lamb, x)* math.exp(-(lamb)))/ math.factorial(x)
        print(simps)
        return simps

    if len(sys.argv) == 3:
        prob(lamb,x)

    if len(sys.argv) == 4:
        in3     =  sys.argv[3]
        sign    =  str(in3)

        if sign == "<":
            for i in range(x):
                probability += prob(lamb, i)


    print(probability)

if __name__=="__main__":
    prob_simpson()



































# import sys
#
# def vowel_recognition():
#     vowels ="aeiouAEIOU"
#     count = 0
#
#     s = sys.argv[1]
#     times= len(s)
#     x=0
#
#     for j in range(times):
#         for i in range(len(s)):
#             check= s[0:(i+1)]
#             for i in range(len(check)):
#                 if check[i] in vowels:
#                     count+=1
#         s= s[(x+1):]
#
#     print("There are {num} vowel sub-strings.".format(num=count))
#     return count
#
#
# if __name__ == "__main__":
#     vowel_recognition()


# a= vowel_recognition("bbbb")
# b= vowel_recognition("baceb")
# c= vowel_recognition("aeiou")
# d= vowel_recognition("aeiouAEIOU")
# e= vowel_recognition("Programfinishesquiggledwithexitcode1PressENTERtsquiggletconsolehedwithexitcode1PressENTEfinsquiggledwithexitcode1PressENTERtoexitconsquigglesolehe")
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
