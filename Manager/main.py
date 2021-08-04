from imports import *

acceptions = ["yes","1","true",
            "sure","absolutely",
            "probably","okay","ok",
            "y", "accept", "mhm", "yep",
            "yuh", "yup", "yeah",
            "yah", "ya", "not no"]


print("Rates : ",
      "\n $.99 if trade <= $10.00",
      "$1.49 if trade <= $25.00",
      "$1.99 if trade <= $50.00",
      "$2.99 if trade <= $200.00",
      "1.49% of trade if trade > $200.00", sep="\n ")


print("\nTrade limit per day = $500")
print("How much would you like to put in?")
amount_putting_in = float(input())


print("Would you like to compensate for the fees?")
if input().lower() in acceptions:
  result = true_fee_value(amount_putting_in)
  print(f"Amount going in = {result['total']}")
  print("The point system works as \n\"   (Fee / Max Value purchaseable with minimum fee) - (Fee / Amount of dollars inputting)\"\nThis allows you to have a 0.0-1.0 amount of point room")
  print(f"Value's minimum fee percentage point = {result['point'] * 10}")

input()