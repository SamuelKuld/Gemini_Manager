def true_fee_value(amount = 0):
  ranges = ({"value" : 10.0,  "fee" : .99, "next" : 25.00}, 
            {"value" : 25.0, "fee" : 1.49, "next" : 50.0}, 
            {"value" : 50.0, "fee" : 1.99, "next" : 200.0}, 
            {"value" : 200.0, "fee" : 2.99, "next" : amount + 1})

  if amount > 200.0:
    return {"total" : amount + ((amount * .0149) * 2), "point" : 0.149}
  if amount < 5.00:
    return {"total" : 0.0, "point" : 0.0}
  if amount >= 5.00 and amount < 10.00:
    return {"total" : amount, "point" : 1}
  for range in ranges:
    if amount >= range["value"] and amount < range["next"]:
        return {"total" : (amount - range["fee"]), 
                "point" : (range["fee"] / range["value"]) - (range["fee"] / amount)}
