import datetime
bookings = {}
total_cars = 10
code = 1
def help():
  help_text = """
    booking: Make a Booking
    display: show all Booking
    search: Search Booking
    cancel: Cancel Booking
    details: show details of the project
    exit: exit\n"""
  print (help_text)
def validate_date(input_date):
  c = input_date.count("-")
  if c != 2 or len(input_date) != 10 or input_date[4] != "-" or input_date[7] != "-":
    return False, "Invalid Format (YYYY-MM-DD)"
  parts = input_date.split("-") # [2020, 12, 15]
  if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
    return False, "should be numbers"
  year, month, day = list(map(int, parts))
  if year < 1 or not (1 <= month <= 12) or not (1 <= day <= 31):
    return False, "Invalid date"
  return True, "Valid date"

def booking():
  global code
  if len(bookings) >= total_cars:
    print("all cars are booked!")
    return
  name = input("enter you name: ")
  start_date = input("start date: ")
  end_date = input("end date: ")
  is_valid, msg = validate_date(start_date)
  if not is_valid:
    print(msg)
    return
  is_valid, msg = validate_date(end_date)
  if not is_valid:
    print(msg)
    return
  start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
  end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
  if start_date > end_date:
    print("Error!")
    return
  new_booking = {
    "name" : name, 
    "satrt_date" : start_date,
    "end_date" : end_date
  }
  bookings[code] = new_booking
  code += 1
  print("Done!")

def cancel(code_del):
  bookings.pop(code_del, "not found!")
  """if code_del in bookings:
    bookings.pop(code_del)
    print("cancelled")
  else:
    print("not found!")"""

def display():
  if len(bookings) != 0:
    for code, booking in bookings.items():
      print(5*"*" + str(code) + 5 * "*")
      print(f"name : {booking['name']}")
      print(f"start date : {booking['satrt_date']}")
      print(f"end date : {booking['end_date']}")
  else:
    print("empty")
def search(code_s):
  if code_s in bookings:
    booking = bookings[code_s]
    print(5*"*" + str(code_s) + 5 * "*")
    print(f"name : {booking['name']}")
    print(f"start date : {booking['satrt_date']}")
    print(f"end date : {booking['end_date']}")
  else:
    print("not found!")
def details():
  pass

while True:
  command = input("Enter your option: ")
  if command == "help":
    help()
  elif command == "booking":
    booking()
  elif command == "display":
    display()
  elif command == "search":
    code_s = int(input("enter your code: "))
    search(code_s)
  elif command == "cancel":
    code_del = int(input("enter your code: "))
    cancel(code_del)
  elif command == "details":
    details()
  elif command == "exit":
    break
  elif command == "":
    continue
  else:
    print("command not found!")