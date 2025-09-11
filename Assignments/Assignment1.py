#Hotel Working Management Information System

# Task 1: Collect Hotel Details from User

# Integer: Hotel ID
hotel_id = int(input("Enter Hotel ID: "))

# String: Hotel Name
hotel_name = input("Enter Hotel Name: ")

# Float: Room Price per Night
room_price = float(input("Enter Room Price per Day: "))

# List: Available Room Types
room_types = input("Enter Room Types (comma-separated): ").split(',')

# Tuple: Total Rooms and Occupied Rooms
total_rooms = int(input("Enter Total Number of Rooms: "))
occupied_rooms = int(input("Enter Number of Occupied Rooms: "))
room_status = (total_rooms, occupied_rooms)

# Float: Tax Percentage
tax_percentage = float(input("Enter Tax Percentage: "))

# Set: Hotel Amenities
amenities = set(input("Enter Amenities (comma-separated): ").split(','))

# Dictionary: Manager Details
manager_name = input("Enter Manager Name: ")
manager_contact = input("Enter Manager Contact Number: ")
manager_location = input("Enter Manager Location: ")
manager_details = {
    "Name": manager_name,
    "Contact": manager_contact,
    "Location": manager_location
}

# Task 2: Display Hotel Details Using Different Formatting Methods

# 1. Comma Separation
print("Hotel ID, Name, Room Price:", hotel_id, hotel_name, room_price, sep=", ")

# 2. Percentage Formatting
print("Tax Applied: %.2f%%" % tax_percentage)

# 3. f-strings
print(f"Hotel Name: {hotel_name}\nRoom Price: ₹{room_price:.2f}\nAvailable Rooms: {room_status[0] - room_status[1]}")

# 4. .format() method
print("Manager Details: Name - {0}, Contact - {1}, Location - {2}".format(
    manager_details["Name"], manager_details["Contact"], manager_details["Location"]
))

# Bonus: Display other data types
print("Room Types:", room_types)
print("Amenities:", amenities)
print("Room Status (Total, Occupied):", room_status)