import argparse
import json
import sys
import datetime
def setup():
    parser = argparse.ArgumentParser(description="weather forecast CLI")
    parser.add_argument("--all", action="store_true", help="Display all data")
    parser.add_argument("--city", type=str, help="Get name of the city")
    parser.add_argument("--forecast",action="store_true", help="forecast 5-days")
    parser.add_argument("--details",action="store_true", help="Display details")
    parser.add_argument("--show-logs",action="store_true", help="show all logs of the program")
    return parser

def load_data():
    with open("weather_data.json", "r") as file:
        data = json.load(file)
    return data

def display_all(data):
    for city, value in data.items():
        print(f"{city}: {value['condition_percent']}% {value['current_condition']}")

def display_forecast(city, data):
    data = data[city]["forecast"]
    print(f"5-day forecast for {city}")
    for day in data:
        print(f" Date: {day['date']}, Condition: {day['condition']}, high: {day['high']}, low: {day['low']}")

def display_details(city, data):
    print(f"Weather details for {city}")
    print(f"  current_condition : {data[city]['current_condition']}")
    print(f"  condition_percent : {data[city]['condition_percent']}%")
    display_forecast(city, data)

def log_command(line):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d")
        file.write(f"{time_now}: {line}\n")

def show_logs():
    with open("commands.log", "r") as file:
        print(file.read())
#.........main.............
parser = setup()
args = parser.parse_args()
command_line = " ".join(sys.argv)
log_command(command_line)
data = load_data()
if args.all:
    display_all(data)
elif args.city:
    name = args.city
    if name not in data:
        print(f"{name}: not found!")
    elif args.forecast:
        display_forecast(name, data)
    elif args.details:
        display_details(name, data)
    else:
        print(f"Currect condition in {name}: {data[name]['current_condition']}")
elif args.show_logs:
    show_logs()



