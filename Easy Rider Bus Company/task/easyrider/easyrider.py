import json
import re

MESSAGE = "Type and required field validation: {} errors"

def main():

    database = json.loads(input())
    errors = {"bus_id" : 0, "stop_id" : 0, "stop_name" : 0, "next_stop" : 0, "stop_type" : 0, "a_time" : 0}
    error_count = 0


    for data in database:
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
        if data["stop_type"] != None:
            if not isinstance(data["stop_type"], str) or len(data["stop_type"]) > 1:
                error_count += 1
                errors["stop_type"] += 1
        if data["a_time"] == None or not isinstance(data["a_time"], str) or not re.match("^\d\d:\d\d$", data["a_time"]):
            error_count += 1
            errors["a_time"] += 1


    print(MESSAGE.format(error_count))
    for field in errors:
        print(field, errors[field], sep=": ")


if __name__ == "__main__":
    main()