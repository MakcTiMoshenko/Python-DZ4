"""*****Напишите функцию , которая будет возвращать переданное в 
качестве параметра n число словами

Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь"""

n = int(input("Введите число: "))

dictNum = {1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
dictTeen = {10:'десять',20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят',60:'шестьдесят',70:'семьдесят',80:'восемьдесят',90:'девяносто'}
dictTeens = {11:'одинадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'девятьнадцать'}
dictHund = {100:'сто',200:'двести',300:'триста',400:'четыреста',500:'пятьсот',600:'шестьсот',700:'семьсот',800:'восемьсот',900:'девятьсот'}
dictTous = {1000:'тысяча', 2000:'две тысячи', 3000:'три тысячи',4000:'четыре тысячи', 5000:'пять тысяч',6000:'шесть тысяч',7000:'семь тысяч',8000:'восемь тысяч',9000:'девять тысяч'}
print(n)

# res = []
# for i in range(len(n)):
#     while n > 0:
#         n = n%10
#         res[i] = n
#         n = n//10
# print(res)

if n == 0:
    print("Нуль")
elif n < 10:
    print(dictNum[n])
elif n == 10 or n == 20 or n == 30 or n == 40 or n == 50 or n == 60 or n == 70 or n == 80 or n == 90:
    print(dictTeen[n])
elif 10 < n < 20:
    print(dictTeens[n])
elif n < 100:
    x = n//10*10
    d = n%10
    print(dictTeen[x] + " " + dictNum[d]) 
elif n == 100 or n == 200 or n == 300 or n == 400 or n == 500 or n == 600 or n == 700 or n == 800 or n == 900:
    print(dictHund[n]) 
elif 100 < n < 110 or 200 < n< 210 or 300 < n < 310 or 400 < n < 410 or 500 < n <510 or 600 < n < 610 or 700 < n < 710 or 800 < n < 810 or 900 < n < 910:
    t = n//100*100
    d = n%10
    print(dictHund[t] + " " + " " + dictNum[d])
elif n == 110 or n == 210 or n == 310 or n == 410 or n == 510 or n == 610 or n == 710 or n == 810 or n == 910: 
    t = n//100*100
    d = n%100
    print(dictHund[t] + " " + " " + dictTeen[d])
elif 110 < n < 120 or 210 < n <220 or 310 < n < 320 or 410 < n < 420 or 510 < n <520 or 610 < n < 620 or 710 < n < 720 or 810 < n < 820 or 910 < n < 920:
    t = n//100*100
    d = n%100
    print(dictHund[t] + " " + " " + dictTeens[d])
elif n == 120 or n == 130 or n == 140 or n == 150 or n == 160 or n == 170 or n == 180 or n == 190:
    t = n//100*100
    d = n%100
    print(dictHund[t] + " " + dictTeen[d])
elif 120 < n < 1000:
    t = n//100*100
    n = n%100
    x = n//10*10
    d = n%10
    print(dictHund[t] + " " + dictTeen[x] + " " + dictNum[d]) 
elif n == 1000 or n == 2000 or n == 3000 or n == 4000 or n == 5000 or n == 6000 or n == 7000 or n == 8000 or n == 9000:
    print(dictTous[n])
elif 1000 < n < 1010 or 2000 < n< 2010 or 3000 < n < 3010 or 4000 < n < 4010 or 5000 < n <5010 or 6000 < n < 6010 or 7000 < n < 7010 or 8000 < n < 8010 or 9000 < n < 9010:
    tou = n//1000*1000
    d = n%10
    print(dictTous[tou] + " " + " " + dictNum[d])
elif 1010 < n < 1020 or 2010 < n< 2020 or 3010 < n < 3020 or 4010 < n < 4020 or 5010 < n <5020 or 6010 < n < 6020 or 7010 < n < 7020 or 8010 < n < 8020 or 9010 < n < 9020:
    tou = n//1000*1000
    d = n%100
    print(dictTous[tou] + " " + " " + dictTeens[d])
elif n == 1020 or n == 2020 or n == 3020 or n == 4020 or n == 5020 or n == 6020 or n == 7020 or n == 8020 or n == 9020:
    tou = n//1000*1000
    d = n%100
    print(dictTous[tou] + " " + " " + dictTeen[d])
elif 1020 < n < 10000:
    to = n//1000*1000
    n = n%1000
    t = n//100*100
    n = n%100
    x = n//10*10
    d = n%10
    print(dictTous[to] + " " + dictHund[t] + " " + dictTeen[x] + " " + dictNum[d])