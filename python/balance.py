# 引入自己的模块实例

# 计算五年复利本息的模块
d=float(input('Please enter what is your initial balance: \n'))
p=float(input('Please input what is the interest rate (as a number): \n'))
d=float(d+d*(p/100))
year=1
while year<=5:
    d=float(d+d*p/100)
    print('Your new balance after year:',year,'is',d)
    year=year+1
print('your final year is',d)