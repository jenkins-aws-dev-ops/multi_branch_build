a = "abc"
print(f'{a}')
a = a.upper()
print(a)
#y = input("enter a number")
x = 2
y = 3
print(y + x)
x = bool(None)
print(x)
cnt = 0
for x in range(1, 10):
    if x % 2 == 0:
        cnt += 1
        print(x)
print(f"we have {cnt} even number...")


def greet():
    print("hello")


greet()


def greeT(name):
    print(f"hello: {name}")


greeT(name="sup")


def op_func(x, by=1):
    return x + by


a = op_func(3, 6)
print(f"{a}")


def mult_argv(*num):
    print(num)
    total = 0
    for n in num:
        total += n
    return total


print(mult_argv(1, 2, 3))


def mult_kw_arg(**user):
    return user


print(mult_kw_arg(name="tom", age=23))


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)
#my_input = int(input("Enter input: "))
# while(my_input != "quit" ):
#   fizz_buzz(my_input)
#    my_input = int(input("Enter input: "))


my_l = ["a", "b"]
my_l.append("y")
my_l.insert(0, "C")
my_l = my_l * 100
print(my_l)
myS = "hello"
a = myS.split()
print(a)
x, y, *other = my_l
print(f"{x} {y}")
print(other)

for ind, i in enumerate(my_l):
    print(ind, {i})
#
