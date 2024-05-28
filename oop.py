class Person:
    # Konstruktor Methode
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def greet(self):
        print(f"Hallo, mein Name ist {self.name}")

class Student(Person):
   def __init__(self,name, age, student_id):
      super().__init__(name, age)
      self.student_id = student_id

   def display_id(self):
      print(f"Meine Student ID ist {self.student_id}")

student1 = Student("Bob", 20, "S12345")

person1 = Person("Alice", 30)
person2 = Person("Tom", 25)

person1.greet()
student1.display_id()
student1.greet()



