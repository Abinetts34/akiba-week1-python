name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("\n================================")
print("           BMI REPORT")
print("================================")

print(f"Name: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height:.2f} m")

print(f"\nBMI: {bmi:.2f}")
print("================================")