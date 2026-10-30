full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")

city = input("Enter your city: ")
university = input("Enter your university: ")
department = input("Enter your department: ")

email = input("Enter your email: ")
phone = input("Enter your phone number: ")
favorite_language = input("Enter your favorite programming language: ")
programming_goal = input("Enter your programming goal")

print("\n" + "=" * 55)
print("              AKIBA STUDENT PROFILE")
print("=" * 55)

print(f"{'Name:':<23} {full_name}")
print(f"{'Student ID:':<23} {student_id}")
print(f"{'Age:':<23} {age}")

print(f"{'City:':<23} {city}")
print(f"{'University:':<23} {university}")
print(f"{'Department:':<23} {department}")

print(f"{'Email:':<23} {email}")
print(f"{'Phone:':<23} {phone}")
print(f"{'Favorite Language:':<23} {favorite_language}")

print("\nProgramming Goal:")
print(programming_goal)

print("=" * 55)
