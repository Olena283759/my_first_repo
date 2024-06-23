# print("Hello world!")
# print("Hello Git")

# num = 8  # приклад значення для num

# if num > 10:
    # print("num більше за 10")
# else:


#x = int(input('Введіть число: '))

#if x % 2 == 0:
    #print("Число x є парним.")
#else:
    #print("Число x є непарним.")

#a = input('Введіть число')
#a = int(a)
#if a > 0:
    #print('Число додатне')
#elif a == 1:
   # print('Число дорівнює 1')
#else:
    #print("a <= 0")

some_num = int(input("please enter the number: "))
if some_num % 5 == 0 and some_num % 2 == 0:
    print("FizzBuzz")
elif some_num % 2 == 0:
    print("Buzz")
elif some_num % 5 == 0:
    print("Fizz")
else:
    print(some_num)