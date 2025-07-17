# Bike Rental Product Information System

# Collecting Product (Bike) Details
bike_id = int(input("Enter Bike ID: "))
bike_name = input("Enter Bike Model Name: ")
price = float(input("Enter Rental Price per Day (₹): "))
categories = input("Enter Bike Categories (comma-separated): ").split(",")
available_bikes_count = int(input("Enter Available Bikes: "))
rented_bikes_count = int(input("Enter Rented Bikes: "))
stock_details = (available_bikes_count, rented_bikes_count)
discount_percentage = float(input("Enter Discount Percentage: "))
features = set(input("Enter Unique Features (comma-separated): ").split(","))
supplier_name = input("Enter Rental Provider Name: ")
supplier_contact = input("Enter Provider Contact Number: ")
supplier_location = input("Enter Provider Location: ")

