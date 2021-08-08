from imports import *
def round_up(value : float):
  if value - abs(value) > 0:
    return math.floor(value) + 1
  else:
    return value