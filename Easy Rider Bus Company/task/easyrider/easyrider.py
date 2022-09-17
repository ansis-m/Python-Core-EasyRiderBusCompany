import json
import re


def minutes(time):
    try:
        hours_and_minutes = time.lstrip("0").split(":")
        return int(hours_and_minutes[0]) * 60 + int(hours_and_minutes[1])
    except:
        print("exception")
        return -1

def main():

    id = 0
    time = 0
    ok = True
    next = False

    print("Arrival time test:")
    for data in json.loads(input()):
        if next and data["bus_id"] == id:
            continue
        next = False
        if data["bus_id"] != id:
            id = data["bus_id"]
        elif time >= minutes(data["a_time"]):
            i = data["bus_id"]
            j = data["stop_name"]
            print(f"bus_id line {i}: wrong time on station {j}")
            ok = False
            next = True
            continue
        time = minutes(data["a_time"])

    if ok:
        print("OK")


if __name__ == "__main__":
    main()