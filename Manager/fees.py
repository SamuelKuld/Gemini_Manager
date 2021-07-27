from imports import *

def true_fee_value(amount = 0):
  counter = (amount * 1.005) - amount
  ranges = ({"value" : 10.0,  "fee" : .99, "next" : 25.0}, 
            {"value" : 25.0, "fee" : 1.49, "next" : 50.0}, 
            {"value" : 50.0, "fee" : 1.99, "next" : 200.0}, 
            {"value" : 200.0, "fee" : 2.99, "next" : amount + 1})
  if amount > 200.0:
    return {"total" : amount + ((amount * .0149) * 2), "point" : 0.149}
  if amount < 5.00:
    return {"total" : 0.0, "point" : 0.0}
  if amount >= 5.00 and amount < 10.00:
    return {"total" : amount * 1.005, "point" : .995}
  for range in ranges:
    if amount >= range["value"] and amount < range["next"]:
        return {"total" : (amount + range["fee"] * 2) + counter, 
                "point" : abs((range["fee"] / amount) - (range["fee"] / range["value"]))}
