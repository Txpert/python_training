fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []

for fruit in fruits:
    output.append(fruit.upper())
    

# Übung 1 - Schreibe den obigen Beispielcode unter Verwendung der List Comprehension-Syntax um. Erstelle eine Variable namens uppercased_fruits, um die Ausgabe der List Comprehension zu speichern. Die Ausgabe sollte ['MANGO', 'KIWI', etc...] sein.
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Übung 2 - Erstelle eine Liste, die jede Frucht mit mehr als 5 Zeichen enthält.
fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_five_characters)

# Übung 3 - Erstelle eine Liste, die jede Frucht mit genau 5 Zeichen enthält.
fruits_with_five_characters = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_five_characters)

# Übung 4 - Erstelle eine Liste, die die Anzahl der Zeichen in jeder Frucht enthält. Die Ausgabe wäre [5, 4, 10, etc...]
number_of_characters_in_fruits = [len(fruit) for fruit in fruits]
print(number_of_characters_in_fruits)

# Übung 5 - Erstelle eine Variable namens fruits_with_letter_a, die eine Liste nur der Früchte enthält, die den Buchstaben "a" enthalten.
fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_letter_a)

# Übung 6 - Erstelle eine Variable namens even_numbers, die nur die geraden Zahlen enthält.
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Übung 7 - Erstelle eine Variable namens odd_numbers, die nur die ungeraden Zahlen enthält.
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

# Übung 8 - Erstelle eine Variable namens positive_numbers, die nur die positiven Zahlen enthält.
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# Übung 9 - Erstelle eine Variable namens numbers_squared, die die Liste der Zahlen enthält, wobei jedes Element quadriert ist. Die Ausgabe lautet [4, 9, 16, etc...]
numbers_squared = [number ** 2 for number in numbers]
print(numbers_squared)

# Übung 10 - Erstelle eine Variable namens odd_negative_numbers, die nur die Zahlen enthält, die sowohl ungerade als auch negativ sind.
odd_negative_numbers = [number for number in numbers if number < 0 and number % 2 != 0]
print(odd_negative_numbers)

# Übung 11 - Erstelle eine Variable namens numbers_plus_5. Darin soll eine Liste zurückgegeben werden, die jede Zahl um fünf erhöht.
numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)
