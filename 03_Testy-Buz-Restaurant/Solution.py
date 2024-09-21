def calculate_delivery_charge(distance):
    # Delivery charges calculation based on distance
    if distance <= 3:
        return 0
    elif distance <= 6:
        return (distance - 3) * 3
    else:
        return 3 * 3 + (distance - 6) * 6

def calculate_bill(food_type, quantity, distance):
    # Check for valid inputs
    if food_type not in menu or quantity < 1 or distance <= 0:
        return -1

    # Get the cost per plate based on food type
    cost_per_plate = menu[food_type][1]

    # Calculate total food cost
    food_cost = cost_per_plate * quantity

    # Calculate delivery charges
    delivery_charge = calculate_delivery_charge(distance)

    return delivery_charge,food_cost

import  random

menu = {'V' :["Veg Combo", 120], 'N' :["Non-Veg Combo", 150]}
welcome_message = f"""Welcom to Testy-Buz Restaurant
Please Enter Food Type
'V' for vegetarian -Rs. {menu['V'][1]} / Plate, 
'N' for non-vegetarian -Rs. {menu['N'][1]} / Plate
"""

print(welcome_message)
food_type = input("Enter Food Type: ").upper()
quantity = int(input("Enter Quantity (Plates): "))
distance = random.randint(0,20)
print(f"Your distance is :{distance} Km.")

bill_amount = calculate_bill(food_type, quantity, distance)
print("===== Your Bill=====")
if bill_amount == -1:
    print(f"Final bill amount: Rs. {bill_amount}")
else:
    print("%-20s%5d"%(menu[food_type][0],bill_amount[1]))
    print("%-20s%5d"%("Delivery Charge",bill_amount[0]))
    print("%-20s%5d" % ("Final bill amount:", bill_amount[0]+bill_amount[1]))
