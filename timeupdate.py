import datetime
import pytz

def getTIME():
    # Get the current time IST
    tz_india = pytz.timezone('Asia/Kolkata')
    current_time_india = datetime.datetime.now(tz_india)

    # Print only the time in a specific format (e.g., HH:MM:SS)
    formatted_time = current_time_india.strftime("%H:%M")
    return formatted_time

def GEThour():
    tz_india = pytz.timezone('Asia/Kolkata')
    current_time_india = datetime.datetime.now(tz_india)
    hour=current_time_india.strftime("%H")

    return hour


