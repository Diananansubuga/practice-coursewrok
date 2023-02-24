
#question1
name=input("Enter your name: ")
age=input("Enter your age: ")

print("hello ", name , "You are ",age, "years old")

#...................................................question2....................................................

def even_numbers(numbers):
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            
            sum += number
    return sum
numbers=[1,2,3,4,5,6,7,8]
print(even_numbers(numbers))

#.......................OR.....................................

numbers= input("Enter a list of numbers ").split(',')
sum = 0

for number in numbers:
    if int(number) % 2 == 0:
        sum += int(number)

print("The sum of even numbers in the list is:", sum)

#........................................................question3..................................................
def words_list(strings):

    words = []
    for string in strings:
        if len(string) > 5:
            words.append(string)
    return words


strings = ["apple", "banana", "orange", "watermelon", "grapefruit", "pear", "peach"]
words = words_list(strings)
print(words)

#...............................................question4..............................................................

item = input("Enter a string: ")
reverse_items = item[::-1]
print("The reverse of the string is:", reverse_items)

#................................................question5..................................................................
def find_unique_elements(input_list):
    unique_elements = []
    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

elements = [1, 2, 3, 3, 4, 4, 5, 6, 6]
unique_elements = find_unique_elements(input_list)
print(unique_elements)
