from client import APODClient
from formatter import format_apod
import sys
import re

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
        
    if len(args) < 2:
        return format_apod(client.get_today())
        
    command = args[1]
    if command == "get_by_date":
        date = _validate_date(args[2])
        return format_apod(client.get_by_date(date))

    if command == "get_random":
        count = _validate_count(args[2])
        return format_apod(client.get_random(count))
        


def _validate_date(date):
    pattern = r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    if not re.search(pattern, date):
        raise ValueError("Invalid date format. Use YYYY-MM-DD. Example: 2026-04-12")
    return date 

def _validate_count(count):
    try:
        count = int(count)
    except ValueError:
        raise ValueError("Count must be an integer.")
    if count <= 0:
        raise ValueError("Count must be greater than 0.")
    return count

if __name__ == "__main__":
    main()

