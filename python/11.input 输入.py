# input 输入
# variable=input() 表示运行后，可以在屏幕中输入一个数字，该数字会赋值给自变量。
a_input=input('please input a number:')
print('this number is:',a_input)

a_input=int(input('please input a number:'))#注意这里要定义一个整数型
if a_input==1:
    print('This is a good one')
elif a_input==2:
    print('See you next time')
else:
    print('Good luck')

# 用input()来判断成绩
score=int(input('Please input your score: \n'))
if score>=90:
   print('Congradulation, you get an A')
elif score >=80:
    print('You get a B')
elif score >=70:
    print('You get a C')
elif score >=60:
    print('You get a D')
else:
    print('Sorry, You are failed ')