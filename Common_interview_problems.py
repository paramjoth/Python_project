#FizzBuzz program, loop through certain numbers and print Fizz if it is divisible by 3 and
#Buzz if it is divisible by 5 and FizzBuzz if it is divisible by both

def fizzbuzz(x):
    for num in xrange(1,x):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

fizzbuzz(15)

#fibonacci series
a,b = 0,1
for x in xrange(10):
    print(a)
    a,b= b, a+b

#prime number
print('following are prime numbers')
for num in xrange(1,50):
    if num>1:
        for x in xrange(2,num):
            if num%x ==0:
                break
        else:
            print(num)
    else:
        print(num)






