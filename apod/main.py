from .client import APODClient
from .formatter import format_apod
import sys
import re
from datetime import date

def main():

    client = APODClient()

    try:
        output = _process_arguments(client, sys.argv)
        if output == None:
            raise ValueError("Invalid arguments.")
    except ValueError as e:
        output = f"Error: {e}"
    except Exception as e:
        output = f"API Error: {e}"

    print(output)
    
def _process_arguments(client, args):
        
    if len(args) == 1:
        return format_apod(client.get_today())
    elif len(args) == 2:
        raise ValueError("Missing arguments.")
    elif len(args) > 3:
        raise ValueError("Too many arguments.")
        
    command = args[1]
    if command == "get_by_date":
        apod_date = _validate_date(args[2])
        return format_apod(client.get_by_date(apod_date))

    if command == "get_random":
        count = _validate_count(args[2])
        return format_apod(client.get_random(count))
        


def _validate_date(apod_date):
    validation = re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", apod_date)
    if not validation:
        raise ValueError("Invalid date format. Use YYYY-MM-DD. Example: 2026-04-12")
    
    year = int(validation.group(1))
    month = int(validation.group(2))
    day = int(validation.group(3))

    input_date = date(year, month, day)
    min_date = date(1995, 6, 16)
    max_date = date.today()

    if input_date < min_date:
        raise ValueError(f"Date cannot be before 1995-06-16. Got: {apod_date}")
    if input_date > max_date:
        raise ValueError(f"Want to travel to the future? Date cannot be after {date.today()}. Got: {apod_date}")
    
    return apod_date 

def _validate_count(count):
    try:
        count = int(count)
    except ValueError:
        raise ValueError("Count must be an integer.")
    if count <= 0:
        raise ValueError("Count must be greater than 0.")
    if count > 10:
        raise ValueError("Maximum 10 requests.")
    return count

if __name__ == "__main__":
    main()

