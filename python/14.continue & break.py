# continue & break

# 跳出循环
# True and False ,当输入1时，a=False时，会执行接下来的语句后再跳出这个循环
a=True
while a:
    b= input('type somesthing')
    if b=='1':
        a= False
    else:
        pass
print ('finish run')


# break 
while True:
    b= input('type somesthing:')
    if b=='1':
        break
    else:
        pass
    print('still in while')
print ('finish run')
# break用法，在循环语句中，使用 break, 当符合跳出条件时，会直接结束循环，这是 break 和 True False 的区别


# continue 
# 直接进入下一次循环
while True:
    b=input('input somesthing:')
    if b=='1':
       continue
    else:
        pass
    print('still in while' )

print ('finish run')