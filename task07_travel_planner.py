destination = input("Enter destination: ")
distance = float(input("Enter distance in kilometers: "))
speed = float(input("Enter average speed in km/h: "))

travel_time = distance / speed

print("\n==================================")
print("          TRAVEL PLANNER")
print("===================================")

print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speed} km/h")

print(f"Estimated Travel Time: {travel_time} hours")
print("===================================")