import datetime
import time
import os

def set_alarm(alarm_time):
    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                print("Wake up!")
                os.system("mpg321 alarm_sound.mp3")  # Play alarm sound (replace "alarm_sound.mp3" with your sound file)
                break
            else:
                print("Current time is", current_time)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Alarm stopped.")

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
