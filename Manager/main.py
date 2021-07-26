import os
# import time

def clear():
  os.system("cls")


def input(input_funct = input):
  return input_funct(">>> ")

print("Rates : ",
      "\n $.99 if trade <= $10.00",
      " $1.49 if trade <= $25.00",
      " $1.99 if trade <= $50.00",
      " $2.99 if trade <= $200.00",
      " 1.49% of trade if trade > $200.00", sep="\n")

print("\nTrade limit per day = $500")
print("How much would you like to put in?")
amount_putting_in = float(input())


def true_fee_value(amount = 0):
  counter = (amount * 1.005) - amount
  ranges = ({"value" : 10.0,  "fee" : .99, "next" : 25.0}, 
            {"value" : 25.0, "fee" : 1.49, "next" : 50.0}, 
            {"value" : 50.0, "fee" : 1.99, "next" : 200.0}, 
            {"value" : 200.0, "fee" : 2.99, "next" : amount + 1})
  if amount > 200.0:
    return amount + ((amount * .0149) * 2)
  if amount < 5.00:
    return 0.0
  for range in ranges:
    if amount >= range["value"] and amount < range["next"]:
        print(f"range = {range}")
        return ((amount + range["fee"] * 2) + counter, abs((range["fee"] / amount) - (range["fee"] / range["value"])))
  

print("Would you like to compensate for the fees?")
if input().lower() in ["yes","1","true","sure","absolutely","probably","okay","ok", "y"]:
  print(f"True value = {true_fee_value(amount_putting_in)[0]}")
  print(f"Value's percentage yield compared to minimum fixed fee = {true_fee_value(amount_putting_in)[1] * 10}")