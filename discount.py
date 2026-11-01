#Lab 5 : discount.py

#Self Assessment: 

# 1. When order_total = 350, the code drops it down tiers. It fails the first if statement, but passes the second Elif statement, and such that discount is applied.
# 2. The difference between the two is that the first has an if statement. If that statement is not included, there can be no further logic within that decision tree.
# 3. Whenever you fill out a credit application or have someone fill it out, the auto_approval feature is based on nothing but if/elif/else statements.

#Exercise 1:

total = float(input("Enter cart total: $"))

#Add your if/elif/else here


#Discount logic
if total >= 500:
    discount = 0.15

elif total >= 200:
    discount = 0.10

elif total >= 100:
    discount = 0.05
else:
    discount = 0

# final = total * (1-discount)

#Exercise 3 
region = "South"
extra_discount = 0
if region == "South" and total >= 100:
    extra_discount = 0.02
print("Region bonus applied: extra 2% off")
final_discount = discount + extra_discount
final = total * (1 - final_discount)

print(f"final_discount: {final_discount:.1%}") #Gives whole percentage not the rate
print(f"Final price: ${final:,.2f}") #give the final at 2 decimals with commas 

#Exercise 2:

if final >1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")


#Exercise 4
customer_type = "wholesale"
# if region =="South":
#     if total > 100:
#         if customer_type == "wholesale":
#             extra_discount = 0.03

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

#Exercise 5

amount = final

if amount < 0:
    print("SUSPICIOUS TRANSACTION")
elif amount < 10000:
    print("NORMAL TRANSACTION")
else:
    print("LARGE TRANSACTION, REVIEW REQUIRED")

#Exercise 6

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False

qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_orders = orders_this_year > 10
vip_upgrade = (qualifies_by_spending or qualifies_by_orders) and not has_outstanding_balance
print(f"VIP Upgrade Status: {vip_upgrade}")