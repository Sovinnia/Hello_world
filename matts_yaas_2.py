# /usr/bin/python

# this one encourages a user to keep working on this stuff with daily reminders

# import the necessary packages
import datetime
import time
import winsound

# define the frequency and duration
frequency = 2500
duration = 1000

# define the time to start the reminder
start_time = datetime.time(9, 0, 0)

# define the time to end the reminder
end_time = datetime.time(17, 0, 0)

# define the time to remind the user
reminder_time = datetime.time(9, 0, 0)

# define the time to remind the user
reminder_time_2 = datetime.time(12, 0, 0)

# define the time to remind the user
reminder_time_3 = datetime.time(15, 0, 0)


def main():
    while True:
        # get the current time
        current_time = datetime.datetime.now().time()
        # check if the current time is between the start and end time
        if start_time <= current_time <= end_time:
            # check if the current time is equal to the reminder time
            if current_time == reminder_time:
                # play the sound
                winsound.Beep(frequency, duration)
                # print the message
                print("It's time to work on your coding!")
            # check if the current time is equal to the reminder time
            if current_time == reminder_time_2:
                # play the sound
                winsound.Beep(frequency, duration)
                # print the message
                print("It's time to work on your coding!")
            # check if the current time is equal to the reminder time
            if current_time == reminder_time_3:
                # play the sound
                winsound.Beep(frequency, duration)
                # print the message
                print("It's time to work on your coding!")
        # sleep for 1 second
        time.sleep(1)


if __name__ == "__main__":
    main()
