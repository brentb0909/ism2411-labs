#Self Reflection 

#1. I was able to spot the bugs without any use of AI. I saw the simple missing colon first, then the sumation, and then the <=[i] error
#2. apply_discount(price,tier) simply means, "Apply a discount to the given price based on the tier of the customer."
#3. If I used AI, I would just cite it like a simple traceback. "AI used on lines 20-30 to debug the apply_discount function, and lines 50-60 to debug the final_price function." This makes it easier to track when someone else needs to troubleshoot. 





#Exercise 1

#define the calculate tax function 

def calculate_tax(price,rate):
    return price * rate

#calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7% : ${tax1:.2f}") 
print(f"Tax on $250 at 8% : ${tax2:.2f}")   


#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
    

#calling the function

price = 200
tiers = {"gold", "silver", "bronze", "none"}

for tier in tiers:
    discounted_price = apply_discount(price, tier)
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

#Exercise 3

#Write it out manually first

# discounted = apply_discount(200, "gold")
# tax = calculate_tax(discounted, 0.07)
# after_tax = discounted + tax
# print(f"After gold discount: ${discounted:.2f}")
# print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"final_price : ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4

orders = {(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")}

for price , tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

#Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1



#Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2
print(x)
print(double_it())
print(x)