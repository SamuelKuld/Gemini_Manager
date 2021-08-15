import os
import datetime
from imports import *


def list_payment_names():
  return [file_name for file_name in os.listdir("/payments/")]

def initialize():
  current_files = os.listdir("/payments/")
  if "payments" not in current_files:
    os.makedir("payments")


def get_current_file_amount():
  current_file_day = f"payments/{datetime.now().strftime('%m-%d-')}"
  current_file_day_amount = 0
  if len(os.listdir("payments/")) > 0:
    for file_name in list_payment_names:
      if file_name.split("-")[0:2] == current_file_day.split("-")[0:2]:
        current_file_day_amount += 1
      else:
        continue
  return current_file_day_amount


def dump(data, file_to_dump_to : str = f"payments/{datetime.now().strftime('%m-%d-%Y')}"):
  with open(file_to_dump_to, "w+") as file:
    pickle.dump(data, file)

def load(file_to_load_from):
  if file_to_load_from not in list_payment_names:
    return None
    
  with open(file_to_load_from, "rw") as file:
    data = pickle.load(file)
  return data

def main():
  initialize()