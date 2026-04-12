from client import APODClient
from formatter import format_apod
import sys
import re

# Fun-fact: Today, 2026-04-06, NASA shared a video of Artemis II trayectory, a mission that 
# will serve as a test for future missions that will land on the moon.

def main():

    client = APODClient()

    try:
        data = None
        output = None

        if len(sys.argv) < 2:
            data = client.get_today() 

        elif sys.argv[1] == "get_by_date":
            try:
                date = sys.argv[2]
                if re.search(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", date):
                    data = client.get_by_date(date)
            except IndexError:
                output = "Date not provided."


        elif sys.argv[1] == "get_random":
            try:
                count = sys.argv[2]
                data = client.get_random(count)
            except IndexError:
                output = "Count not provided."

        
        if data != None:
            output = format_apod(data)
        if output == None:
            output = "Invalid arguments received."
    
    except Exception as e:
        output = f"Error: {e}"
        

    print(output)

if __name__ == "__main__":
    main()

