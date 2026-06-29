# CAR MILEAGE CALCULATOR

print("CAR MILEAGE CALCULATOR")

# ENTER VEHICLE NAME
vehicle_name = input("\nENTER YOUR VEHICLE NAME: ")

# ENTER DISTANCE TRAVELLED
distance_travelled = float(input("ENTER DISTANCE TRAVELLED BY VEHICLE (in KM): "))

if distance_travelled <= 0:
    print("Distance must be greater than 0.")

# ENTER FUEL USED
fuel_used = float(input("ENTER FUEL USED (in litres): "))

if fuel_used <= 0:
    print("Fuel used must be greater than 0.")

# SELECT FUEL TYPE
print("\nSELECT FUEL TYPE:")
print("1. Petrol")
print("2. Diesel")
print("3. CNG")

fuel_choice = input("Enter your choice (1/2/3): ")

if fuel_choice == "1":
    fuel_type = "Petrol"
elif fuel_choice == "2":
    fuel_type = "Diesel"
elif fuel_choice == "3":
    fuel_type = "CNG"
else:
    fuel_type = "Unknown"
    print("Invalid Fuel Type!")

# ENTER FUEL PRICE
fuel_price = float(input("Enter Fuel Price per litre (₹): "))

if fuel_price <= 0:
    print("Fuel price must be greater than 0.")

# CALCULATIONS
mileage = distance_travelled / fuel_used
trip_cost = fuel_used * fuel_price
cost_per_km = trip_cost / distance_travelled

# RESULT
print("\n========== RESULT ==========")
print("Vehicle Name :", vehicle_name)
print("Fuel Type    :", fuel_type)
print("Distance     :", distance_travelled, "KM")
print("Fuel Used    :", fuel_used, "Litres")
print("Mileage      :", mileage, "km/L")
print("Fuel Price   : ₹", fuel_price)
print("Trip Cost    : ₹", trip_cost)
print("Cost per km  : ₹", cost_per_km)
print("============================")

print("\nTHANK YOU FOR USING CAR MILEAGE CALCULATOR")
print("MADE BY KARTHIK ")