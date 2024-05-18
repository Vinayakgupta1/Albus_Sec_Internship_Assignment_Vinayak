# Q.4 Create a class programmer for storing information of few programmers working at Microsoft.

class Programmer:
  def __init__(self, employee, language, position):
      self.employee = employee
      self.language = language
      self.position = position

  def result(self):
      return f"{self.employee} with {self.language} programming language at {self.position} position is working at Microsoft."

employee = input("Enter the name of Employee at Microsoft : ")
language = input("Enter the Prefered Programming Language : ")
position = input("Enter the position at Microsoft : ")
result = Programmer(employee, language, position)
print(result.result())

