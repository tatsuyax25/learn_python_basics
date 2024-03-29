print("Hello, World!")

# Primitive Data Types
# String Example
name = "Miguel"
# Integer Example
age = 41
# Float Example
height = 1.77
# Boolean Example
is_student = False
# Print variable values
print(name)
print(age)
print(height)
print(is_student)

# Non-Primitive Data Types
# List Example
fruits = ["Apple", "Banana", "Orange"]
print("List Example:", fruits)

# Tuple Example
coordinates = (10, 20)
print("Tuple Example:", coordinates)

# Dictionary Example
person = {
  "name": "Miguel",
  "age": 41,
  "is_student": False,
}
print("Dictionary Example:", person)

# Arithmetic Operations
num1 = 10
num2 = 3
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
mod_result = num1 % num2
exp_result = num1 ** num2
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Exponentiation:", exp_result)

# Comparison Operations
age = 41
is_adult = age >= 18
is_teenager = age >= 13 and age < 18
print("Is Adult:", is_adult)
print("Is Teenager:", is_teenager)

# Conditional Statements
age = 20
if age < 18:
  print("You are a minor.")
elif 18 <= age < 21:
  print("You are an adult, but not yet allowed to drink.")
else:
  print("You are a legal adult.");

# for Loop
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
  print(fruit)

# While Loop
count = 0
while count < 5:
  print("Count:", count)
  count += 1

# Break Statement
print("Output with 'break':")
for i in range(5):
  if i == 3:
    print(f"Encountered 'break' at i={i}")
    break
  print(i)

# Continue Statement
print("\nOutput with 'continue':")
for i in range(5):
  if i == 2:
    print(f"Skipped iteration with 'continue' at i={i}")
    continue
  print(i)

# Function
def greet():
  print("Hello, World!")
# Call the function to execute
greet()

def check_age(age):
  if age < 18:
    print("You are a minor.")
  elif 18 <= age < 21:
    print("You are an adult, but not yet allowed to drink.")
  else:
    print("You are a legal adult.")

# Call the function with a specific age
check_age(20)