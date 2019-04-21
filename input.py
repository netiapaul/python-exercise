# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

age=int(input('what your age? '))
name=input('Whats your name? ')
year=int((2019-age)+100)
print( name.title() + ' will be 100 year in ' + str(year))

# 2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

number=int(input('Enter any number: '))

if number % 2 == 0:
    print('Thats  an even number')
else:
    print('Thats an odd number')

#3.  Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

lists = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist=[]

for l in lists:
    if l <= 5:
        newlist.append(l)
        print(newlist)

#4.  Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

numb=int(input('Enter a number to find its divisor: '))
listarnge=list(range(1,21))
divisor=[]
for div in listarnge:
    if numb % div == 0:
        divisor.append(div)
        print(divisor)


#5. Take two lists nd write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


list1=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newlist=[]

for num in list2:
    if num in list1:
        newlist.append(num)
        print(num)

#another solution
a = [1,1,1,6,7,8,9,4,9]
b = [1,6,87,98,67,45,10,11,12,13,14,15,16]
print(set(a) & set(b))

# 6.  Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

# 7. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
evenlist=[]

for num in a:
    if num % 2 == 0:
        evenlist.append(num)
        print(evenlist)

#8. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

number=random.randint(1,9)
print(number)

guess=0

while guess != 'quit' or guess != number:
    guess=input("Write number between 1 and 9:  \n enter 'quit' to end game: ")

    if guess == 'quit':
        break

    guess=int(guess)

    if guess < number:
        print('Too low')
    elif guess > number:
        print('Way too high')
    else:
        print('You are on point')
