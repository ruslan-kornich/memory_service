import time

import psutil
import requests

url = "http://localhost:8080"


def send_alarm(url_request, data):
    response = requests.post(url_request, data=data)
    if response.status_code == 200:
        return True
    return False


def main():
    try:
        memory_control = int(input("Set memory control in kilobytes( e.g. 5000) : "))
        while True:
            value = psutil.virtual_memory()
            print(f"You used {value.used / 1_000_000} Kb")
            if value.used > memory_control:
                data_dict = {"value_used": f"{int(value.used / 1_000_000)} Kb"}
                if send_alarm(url, data=data_dict):
                    print("Made an entry in the database about memory overrun")
            time.sleep(10)
    except ValueError:
        print("Reboot and enter a numeric value please")


if __name__ == "__main__":
    main()
