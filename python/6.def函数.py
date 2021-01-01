# def 函数
def function():
    print('This is a function')
    a = 1+2
    print(a)

function()

# 函数参数
def func(a, b):
    c = a+b
    print('the c is ', c)
func(1,2)
# 如果我们忘记了函数的参数的位置，只知道各个参数的名字，可以在函数调用的过程中给指明特定的参数 func(a=1, b=2), 
# 这样的话，参数的位置将不受影响，所以 func(b=2,a=1) 是同样的效果。

# 函数默认参数
def sale_car(price, color='red', brand='carmy', is_second_hand=True):
    print('price', price,
          'color', color,
          'brand', brand,
          'is_second_hand', is_second_hand,)
sale_car(1000)
# 如果我们调用函数 sale_car(1000), 那么与 sale_car(1000, 'red', 'carmy', True) 是一样的效果。
# 当然也可以在函数调用过程中传入特定的参数用来修改默认参数。通过默认参数可以减轻我们函数调用的复杂度。

# 自调用
# 如果想要在执行脚本的时候执行一些代码，比如单元测试，可以在脚本最后加上单元测试代码，
# 但是该脚本作为一个模块对外提供功能的时候单元测试代码也会执行，这些往往我们不想要的，我们可以把这些代码放入脚本最后：
# if __name__ == '__main__':
    #code_here
# 如果执行该脚本的时候，该 if 判断语句将会是 True,那么内部的代码将会执行。
# 如果外部调用该脚本，if 判断语句则为 False,内部代码将不会执行。


# 可变参数
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)
report('Mike', 8, 9)

# 关键字参数
def portrait(name, **kw):
    print('name is', name)
    for k,v in kw.items():
        print(k, v)
portrait('Mike', age=24, country='China', education='bachelor')
# 通过可变参数和关键字参数，任何函数都可以用 universal_func(*args, **kw) 表达。
