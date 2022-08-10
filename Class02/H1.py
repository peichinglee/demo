
"""
##第一題
import math

try:
    X = int(input("X= "))
    Y = int(input("Y= "))
    Z = X/Y
    print(math.ceil(Z * 100) / 100)
except ValueError:
    print("請輸入正確數字格式")

##第二題
try:
    num = int(input("Number: "))
    if num % 6 ==0:
        print(f"{num} 為 6 的倍數")
    elif num % 6 !=0:
        if num % 3 ==0:
            print(f"{num} 為 3 的倍數")
        elif num % 2 ==0:
            print(f"{num} 為 2 的倍數")
        else:
            print(f"{num} 非2、3、6倍數")
except ValueError:
    print("請輸入正確數字格式")

##第三題
t = int(input("請輸入n秒(n<86400)："))
if t<=86400:
    sec = (t % 60**2) % 60
    min = (t % 60**2) // 60
    hr = t // 60**2
    print(f"{hr}時 {min}分 {sec}秒")
else:
    sec = (t % 60**2) % 60
    min = (t % 60**2) // 60
    hr = (t % 86400)//(60**2)
    day =  t//86400
    print(f"{day}天 {hr}時 {min}分 {sec}秒")

##第四題
num = int(input("輸入偶數: "))
if num % 2 ==0:
    i=1
    while i < num:
        if i % 2 !=0:
            print(i, end=" ")
        i += 1
else:
    print(f"{num} 非偶數")


"""
n = int(input())
import random
ans =[random.randint(1,100) for i in range(n)]
print(ans)
