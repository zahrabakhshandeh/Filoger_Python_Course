# Importing necessary liberaries
import datetime

# Dictionary to save booking information
bookings = {}
# Constant for total number of cars
total_cars = 10
# Variable to generate unique booking codes
code = 1

# ----------------Functions----------------
# Function to display help information
def help():
  help_text = """
    booking: Make a Booking
    display: show all Booking
    search: Search Booking
    cancel: Cancel Booking
    
    details: show details of the project
    exit: exit\n"""
  print (help_text)

# Function to validate the date entered by the user
def validate_date(input_date):
  c = input_date.count("-")
  # Check format of date
  if c != 2 or len(input_date) != 10 or input_date[4] != "-" or input_date[7] != "-":
    return False, "Invalid Format (YYYY-MM-DD)"
  # Check if year, month, and day are all digits
  parts = input_date.split("-") # [2020, 12, 15]
  if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
    return False, "should be numbers"
  # Validate the range of year, month, and day
  year, month, day = list(map(int, parts))
  if year < 1 or not (1 <= month <= 12) or not (1 <= day <= 31):
    return False, "Invalid date"
  return True, "Valid date"

def find_days(start_date, end_date):
  if start_date == end_date:
    return 0
  else:
    new_start_date = start_date + datetime.timedelta(days=1)
    return 1 + find_days(new_start_date, end_date)
# Function to handle booking of cars
def booking():
  global code # Declare code as global since we're modifying it
  # Check if all cars are already booked
  if len(bookings) >= total_cars:
    print("all cars are booked!")
    return
  name = input("enter you name: ")
  start_date = input("start date: ")
  end_date = input("end date: ")
  # Validate the provided dates
  is_valid, msg = validate_date(start_date)
  if not is_valid:
    print(msg)
    return
  is_valid, msg = validate_date(end_date)
  if not is_valid:
    print(msg)
    return
  # Convert string dates to datetime
  start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
  end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
  count_days = end_date - start_date
  count_days = count_days.days
  res = find_days(start_date, end_date)
  print(res, count_days)
  # Check if the end date comes before the start date
  if start_date > end_date:
    print("Error!")
    return
  # Create new booking
  new_booking = {
    "name" : name, 
    "start_date" : start_date,
    "end_date" : end_date,
    "days" : count_days
  }
  print(new_booking)
  # save with new code
  bookings[code] = new_booking
  # Increment the booking code for the next booking
  code += 1
  print("Done!")

# Function to cancel a booking
def cancel(code_del):
  bookings.pop(code_del, "not found!")

# Function to display all current bookings
def display():
  if len(bookings) != 0:
    for code, booking in bookings.items():
      print(5*"*" + str(code) + 5 * "*")
      print(f"name : {booking['name']}")
      print(f"start date : {booking['start_date']}")
      print(f"end date : {booking['end_date']}")
      print(f"days : {booking['days']}")
  else:
    print("empty")

# Function to search for a booking using its code
def search_by_code(code_s):
  if code_s in bookings:
    booking = bookings[code_s]
    print(5*"*" + str(code_s) + 5 * "*")
    print(f"name : {booking['name']}")
    print(f"start date : {booking['start_date']}")
    print(f"end date : {booking['end_date']}")
    print(f"days : {booking['days']}")
  else:
    print("not found!")

def search_by_name(name):
  found = False
  for code, booking in bookings.items():
    if booking["name"] == name:
      print(5*"*" + str(code) + 5 * "*")
      print(f"name : {booking['name']}")
      print(f"start date : {booking['start_date']}")
      print(f"end date : {booking['end_date']}")
      print(f"days : {booking['days']}")
      found = True
  if not found:
    print(f"{name}: not found!")
  

def search():
  cmd = input("search by 'name' or 'code': ")
  if cmd == "name":
    name = input("name for search: ")
    search_by_name(name)
  if cmd == "code":
    code_s = int(input("code for search: "))
    search_by_code(code_s)
  else:
    print("not found!")

# Details to show a details of the cars
def details():
  num_booked_cars = len(bookings)
  num_available_cars = total_cars - num_booked_cars
  print(f"Total number of cars: {total_cars}")
  print(f"number of booked: {num_booked_cars}")
  print(f"number of availabel: {num_available_cars}")

# ----------------Main----------------
while True:
  command = input("Enter your option: ")
  if command == "help":
    help()
  elif command == "booking":
    booking()
  elif command == "display":
    display()
  elif command == "search":
    search()
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