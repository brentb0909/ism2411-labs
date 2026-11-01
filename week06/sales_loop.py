#self reflection
#1. The accumulator pattern is simple. First, you have to initialize a variable to start your count. Then, you create a loop to keep adding to said count. Finally, you print at the end outside of the loop for your final total.
#2. I noticed that the code was much shorter, but because of that, its harder to customize with smaller details.
#3. I think an easy loop would be how many tickets were sold for a park. You could see how much of each tier was being sold along with total tickets and income. 



#Exercise 1 

sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0   #initialization 

for sale in sales: 
    total += sale    #update

print(f"Total: ${total}") 

#Exercise 2

total = 0
count = 0
for sale in sales:
    total += sale
    count += 1
average = total / count
print(f"total: ${total }")    
print(f"count: {count}")
print(f"average: ${average:.2f}")

 #Exercise 3

current_max = sales[0]
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")


#Exercise 4

count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Number of sales over $100: {count_over_100}")
print(f"Total of sales over $100: ${total_over_100}")

#Exercise 5

for sale in sales:
    if sale > 400:
        print(f"Alert: Outlier found - ${sale}. Stopping.")
        break
    if sale < 100:
        continue
print(f"${sale}") 

#Exercise 6

total = 0
i = 0      #index 
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total (while loop): ${total}")

#Excercise 7

for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:   
        discount = 0.0 
discounted_price = sale * (1 - discount)
print(f"{discount*100:.0f}% discount")
print(f"Discounted price: ${discounted_price:.2f}")

