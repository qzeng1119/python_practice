# sentence = "i want to sleep right now!"
# print(sentence.islower())
# print(len(sentence))
# print(sentence[3])
# print(sentence.replace("sleep","eat something"))
# import math
# print(math.floor(9.5))
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello, " + name + "! You are " + age + " this year!")

# array = ["Mike", 5]
# arr = [False]
# array[0] = "John"
# array.extend(arr)
# array.append("who")
# array.insert(1,7)
# array.remove("John")
# array.pop()
# print(array)
# num = array.(False) + 1
# print(num)

# lists = [(1,4), 1, True]
# print(lists)
# print(lists[0])
# print(lists[0][1])

# def cube(num):
#     return num*num*num
# print(cube(3))

# array = []
# num = input("Enter a number: ")
# array.append(num)
# num = input("Enter another number: ")
# array.append(num)
# print(array)

# is_male = False
# is_tall = True
# if is_male and is_tall:
#     print("You are a tall man")
# elif is_male and not(is_tall):
#     print("You are a short man")
# elif not(is_male) and is_tall:
#     print("You are a tall woman")
# else:
#     print("You are a short woman")

# i = 0
# while i < 10:
#     i += 1
#     print(i)
# print("loop finished")

# for index in range(10):
#     print(index)

# for index in range(3,10):
#     print(index)

# friends = ["Jerry", "Julie", "Mike"]
# for index in range(len(friends)):
#     print(friends[index])

# print(4**3) # equal to 4^3

'''
def translate(phrase): # function: convert each vowel to "g" in the phrase
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation
to_be_translated = input("Enter the phrase to be translated: ")
print(translate(to_be_translated))
'''

'''
try:
    number = int(input("Enter a number: "))
    print(number)
except: # when any errors appear in the "try:" part, the "except:" part will be executed
    print("Invalid Input")
'''

# diary_file = open("diary.txt", "r")
# print(diary_file.readlines()[1])
# diary_file.close()

'''
class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self): # class function, can be called by the object of this class
        if self.gpa >= 3.5:
            return True
        else:
            return False
student1 = Student("Pam", 19, "math", 3.0)
print(student1.on_honor_roll())
'''