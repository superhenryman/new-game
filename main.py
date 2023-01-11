import  time
def calculate():
   x = input('''
Please type in the math operation you would like to do:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
   y = float(input("Please write your first number: "))
   z = float(input("Please write your second number: "))

   if x == "+":
    print(y + z)
   elif x == '-':
    print(y - z)
   elif x == '*':
    print(y * z)
   elif x == '/':
    print(y / z)
   else:
       print("You have not written the right operator right please restart the program")
calculate()
time.sleep(10)
print("Close this")
