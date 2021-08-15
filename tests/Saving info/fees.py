from imports import *

def true_fee_value(amount = 0):
  ranges = ({"value" : 10.0,  "fee" : .99, "next" : 25.00}, 
            {"value" : 25.0, "fee" : 1.49, "next" : 50.0}, 
            {"value" : 50.0, "fee" : 1.99, "next" : 200.0},
            {"value" : 200.0, "fee" : (amount * .981), "next" : amount + 1},)

  if amount > 200.0:
    return {"total" : amount - (amount * .0149), 
            "point" : 0.149,
            "amount" : amount,}

  if amount < 5.00:
    return {"total" : 0.0, 
            "point" : 0.0,
            "amount" : amount,}

  if amount >= 5.00 and amount < 10.00:
    return {"total" : amount, 
            "point" : 1,
            "amount" : amount,}

  if amount < 200.0:
    for range in ranges:
      if amount >= range["value"] and amount < range["next"]:
          return {"total" : (amount - range["fee"]), 
                  "point" : ((range["fee"] / amount) * 100),
                  "amount" : amount,}

  if amount >= 200:
    return {"total" : (amount * .981), 
            "point" : (1.9),
            "amount" : amount,}


print(true_fee_value(200))
