#Hotel Working Management Information System

#Collecting information(Hotel)  System
hotel_name = input("Enter Hotel Name:")
total_rooms_count = int(input("Enter total rooms: "))
filled_rooms_count =int(input("Enter filled rooms :"))
available_rooms_count =int(input("Enter available rooms :"))
categories =input("Enter different rooms categories:")
price = int(input("Enter AC rooms price per day:"))
price = int(input("Enter non AC room price per day:"))
supplier_name = input("Enter room provider name:")
supplier_contact = input("Enter room provider contact number:")
supplier_location = input("Enter provider location:")

supplier_details = {
    "name": supplier_name,
    "contact":supplier_contact,
    "location":supplier_location
}

#Displaying the hotel working management system by different formatting methods

print("\n-- Hotel working management system ---\n")

print("Hotel Name:",hotel_name)
print("Total Rooms:",total_rooms_count)
print("Booked Rooms:",filled_rooms_count)
print("available rooms:",available_rooms_count)
print("Rooms Categories:",categories)
print("AC rooms price per day:",price)
print("Non AC rooms price per day:",price)
print("Details of supplier:",supplier_name,supplier_contact,supplier_location)


