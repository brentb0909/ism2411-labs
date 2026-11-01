#inventory.py
#Author: Brent Barnes


#Reflection 1
#I think that tuples shocked me the most, but they makes sense. I think that its important to have a way to store data that you cant mess up.

#Reflection 2
#I had to do a large report for a business class, and lists would have been a much more simple way to store all of the data I was working on.

print("--- Exercise 1: Build the list ---")
inventory = ["pen","notebook", "stapler", "tape", "market"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #first item
print(inventory[-1]) #last item
middle = len(inventory) // 2
print(inventory[middle]) #middle item

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) #first three items
print(inventory[-2:]) #last two items
print(inventory[::2]) #every other item

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope") #add an item to the end of the list
print(inventory)
inventory.remove("tape") #remove an item from the list
print(inventory)
inventory.sort() #sort the list in alphabetical order
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) #tuple of coordinates

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never be changed by accident")

print(coords)

print("--- Exercise 6: Average List of sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total/count 
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")   

      
