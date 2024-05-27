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

# Übung 2 - Erstelle eine Liste, die jede Frucht mit mehr als 5 Zeichen enthält.

# Übung 3 - Erstelle eine Liste, die jede Frucht mit genau 5 Zeichen enthält.

# Übung 4 - Erstelle eine Liste, die die Anzahl der Zeichen in jeder Frucht enthält. Die Ausgabe wäre [5, 4, 10, etc...]

# Übung 5 - Erstelle eine Variable namens fruits_with_letter_a, die eine Liste nur der Früchte enthält, die den Buchstaben "a" enthalten.

# Übung 6 - Erstelle eine Variable namens even_numbers, die nur die geraden Zahlen enthält.

# Übung 7 - Erstelle eine Variable namens odd_numbers, die nur die ungeraden Zahlen enthält.

# Übung 8 - Erstelle eine Variable namens positive_numbers, die nur die positiven Zahlen enthält.

# Übung 9 - Erstelle eine Variable namens numbers_squared, die die Liste der Zahlen enthält, wobei jedes Element quadriert ist. Die Ausgabe lautet [4, 9, 16, etc...]

# Übung 10 - Erstelle eine Variable namens odd_negative_numbers, die nur die Zahlen enthält, die sowohl ungerade als auch negativ sind.

# Übung 11 - Erstelle eine Variable namens numbers_plus_5. Darin soll eine Liste zurückgegeben werden, die jede Zahl um fünf erhöht.