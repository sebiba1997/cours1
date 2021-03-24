# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   """Cette fonction additionne deux nombres et retourne la somme de ces derniers.
   
   :param int x: Premier nombre
   :param int y: Second nombre
   
   :returns: Somme des deux nommbres
   :rtype: int"""

   return x + y

def subtract(x, y):
   """Cette fonction soustrait deux nombres et retourne la différence de ces derniers.
   
   :param int x: Premier nombre
   :param int y: Second nombre
   
   :returns: Différence entre les deux nommbres
   :rtype: int"""

   return x - y

def multiply(x, y):
   """Cette fonction multiplie deux nombres et retourne la multiplication de ces derniers.
   
   :param int x: Premier nombre
   :param int y: Second nombre
   
   :returns: Multiplication des deux nommbres
   :rtype: int"""

   return x * y

def divide(x, y):
   """Cette fonction divise deux nombres et retourne la quotient de ces derniers.
   
   :param int x: Premier nombre
   :param int y: Second nombre
   
   :returns: Quotient des deux nommbres
   :rtype: float"""

   return x / y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")