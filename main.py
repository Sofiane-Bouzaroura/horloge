import time
import threading

def horloge(hour, minute, second, alarm_time):
    while True:
        
        current_time = f"{hour:02d}:{minute:02d}:{second:02d}"
        print(current_time, end="\r")

        time.sleep(1)

        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0
        if (hour, minute, second) == alarm_time:
            print("\nAlarme!")
        

def alarme():
    hour = int(input("Entrer l'heure de l'alarme (0-23) : "))
    minute = int(input("Entrer les minutes de l'alarme (0-59) : "))
    second = int(input("Entrer les secondes de l'alarme (0-59) : "))
    
    return hour, minute, second


if __name__ == "__main__":
    print("Réglage de l'heure actuelle :")
    current_hour = int(input("Entrer l'heure actuelle (0-23) : "))
    current_minute = int(input("Entrer les minutes actuelles (0-59) : "))
    current_second = int(input("Entrer les secondes actuelles (0-59) : "))

    alarm_time = alarme()

    horloge_thread = threading.Thread(target=horloge, args=(current_hour, current_minute, current_second, alarm_time))

    horloge_thread.start()  
