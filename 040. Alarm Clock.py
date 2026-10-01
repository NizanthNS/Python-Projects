# Python Alarm Clock

import time
import datetime
import sounddevice as sd
import soundfile as sf

def set_alarm(target_time):
    print(f"Alarm Set for : {target_time}")

    sound_file = "D:/Test_Audio/After Dark.mp3"

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(f"\rCurrent Time : {current_time}", end = " ")

        if current_time == target_time:
            print("\nWake UP!")

            try:
                data, samplerate = sf.read(sound_file)
                sd.play(data, samplerate)
                sd.wait()

            except Exception as e:
                print(f"ERROR Playing Sound : {e}")

            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the Alarm Time (HH:MM:SS) : ")
    set_alarm(alarm_time)