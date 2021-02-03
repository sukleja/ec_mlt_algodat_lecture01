import array as arr
import time as time

# Examples for programming basics and Python

# Data type assignment and operators
# integer
x = 1
y = 2

x, y, z = 1, 2, 3

# arithmetic operators
z = x + y
z = x - y
z = x * y
z = y ** 2
z = x / y

# float, what problems could floating point numbers introduce?
xf = 1.0
yf = 2.0

# string
text1 = "Hello"
text2 = "World"

# boolean
check1 = True
check2 = False

# type casts
string_x = str(x)
int_bool = int(check1)

# type annotation
xi: int = 1
df: float = 1
text_a: str = "text"


def hello_world(name):
    print("Hello " + name)  # string concatenation
    # print(f'Hello {name}')      #variant of concatenation can accepts other data types
    # print("Hello "+"\n"+name)   #newline
    # print("Hello \nWorld")      #escape sequence
    # print(r"Hello \nWorld")     #raw input

    # print("Hello "+x)
    # print("Hello " + str(x))

    # print(int_bool)
    # print(check1)
    # print(type(x))


# integer funtion with two integer parameters
def sum_two_numbers(num1: int, num2: int):
    sum = num1 + num2
    return sum


# with return type annotation
def concat_string(word1: str, word2: str) -> str:
    result = word1 + word2
    return result


# control stuctures
def odd_or_even(num: int):
    if num % 2 == 0:
        print("The number: " + str(num) + " is even")
    else:
        print("The number " + str(num) + " is odd")


# multiple conditions
def salary_level(money: int):
    if money < 1000:
        print("Poor")
    elif 1000 < money < 4999:
        print("Average")
    elif 5000 < money < 10000:
        print("Rich")
    else:
        print("Very Rich")


# Scope
i = 0


def scope():
    i = 100
    print("Variable i :" + str(i))


# while loop, what problems can arise in a while loop
def loop(num: int):
    while num > 0:
        print(num)
        num -= 1


# simple range loop
def loop_numbers(num: int):
    for i in range(num):
        print(i + 1)


# tuple unpacking and enumerate()
def tuple_unpacking():
    lst = ['A', 'B', 'C']
    for index, value in enumerate(lst):
        print(index, value)


# looping over an array
def loop_list():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # lst="test"
    x = 0
    for i in lst:
        print(i)
        x += 1


# break / continue
def loop_break():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in lst:
        if i != 4:
            print(i)
        else:
            break


def loop_cont():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in lst:
        if i != 4:
            print(i)
        else:
            continue


# variable pointers on mutable collections
def reference():
    a = [1, 2, 3]
    b = a
    b[0] = 0
    print("a: " + str(a))
    if a is b:
        print("Both point to the same memory location")
    else:
        print("These are two different objects")


# checking data types
def data_types(data):
    x = type(data)
    print(type(data))
    print(isinstance(data, float))


# Generators
def odd_gen(j):
    i = 1
    while i < j:
        yield i
        i += 2


def odd_lst(j):
    i = 1
    lst = []
    while i < j:
        lst.append(i)
        i += 2
    return lst


if __name__ == '__main__':  # only executes if our file is the main program
    # scope()

    # name = input("Enter your name: ")
    # print("Your name ist: " + name)
    data_types(1)
    data_types(2.0)
    data_types("text")
    reference()
    print(concat_string.__annotations__)  # show annotations

    # demonstrate generators
    new_arr = arr.array('i', [1] * (10 ** 6))
    t1 = time.time()
    x = odd_gen(10)
    print("%.6f" % (time.time() - t1))
    t1 = time.time()
    y = odd_lst(10)
    print("%.6f" % (time.time() - t1))

    # iterate over iterator object
    for i in x:
        print(i, end=" ")
    print('\n')

    tuple_unpacking()

############################################################
# binary, hexadecimal and octal
bin = 0b10
hex = 0x10
oct = 0o10

# complex
cplx = 3 + 4j
############################################################
