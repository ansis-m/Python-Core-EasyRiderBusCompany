import json
import re

MESSAGE = "Type and required field validation: {} errors"

def main():

    errors = {"bus_id" : 0, "stop_id" : 0, "stop_name" : 0, "next_stop" : 0, "stop_type" : 0, "a_time" : 0}
    error_count = 0

    for data in json.loads(input()):
        if data["bus_id"] == None or not isinstance(data["bus_id"], int) or data["bus_id"] < 0:
            error_count += 1
            errors["bus_id"] += 1
        if data["stop_id"] == None or not isinstance(data["stop_id"], int) or data["stop_id"] < 0:
            error_count += 1
            errors["stop_id"] += 1
        if data["stop_name"] == None or not isinstance(data["stop_name"], str) or len(data["stop_name"]) == 0:
            error_count += 1
            errors["stop_name"] += 1
        if data["next_stop"] == None or not isinstance(data["next_stop"], int) or data["next_stop"] < 0:
            error_count += 1
            errors["next_stop"] += 1
        if data["stop_type"] != None and data["stop_type"] != "":
            if not isinstance(data["stop_type"], str) or len(data["stop_type"]) > 1 or not re.match("[SOF]", data["stop_type"]):
                error_count += 1
                errors["stop_type"] += 1
        if data["a_time"] == None or not isinstance(data["a_time"], str) or not re.match("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", data["a_time"]):
            error_count += 1
            errors["a_time"] += 1

    print(MESSAGE.format(error_count))
    for field in errors:
        if errors[field] > 0:
            print(field, errors[field], sep=": ")


if __name__ == "__main__":
    main()