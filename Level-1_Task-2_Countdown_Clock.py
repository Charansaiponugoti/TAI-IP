import datetime
import time

def countdown(end_datetime):
    while True:
        now = datetime.datetime.now()
        remaining_time = end_datetime - now
        if remaining_time.days < 0:
            print("Countdown expired!")
            break
        print(f"Countdown: {remaining_time.days} days, {remaining_time.seconds // 3600} hours, {remaining_time.seconds // 60 % 60} minutes, {remaining_time.seconds % 60} seconds")
        time.sleep(1)

# Example usage:
end_datetime = datetime.datetime(2024, 3, 2, 23, 0, 0)  # set the end date and time here
countdown(end_datetime)

