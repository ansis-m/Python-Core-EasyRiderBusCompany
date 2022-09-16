import json
import re

MESSAGE = "Type and required field validation: {} errors"

def bad_name(stop_name):

    tokens = re.split("\s", stop_name)
    if len(tokens) < 2 or tokens[-1] not in ["Road", "Avenue", "Street", "Boulevard"]:
        return True
    for token in tokens:
        if not re.match("[A-Z][a-z]+", token):
            return True
    return False

def main():

    # errors = {"bus_id" : 0, "stop_id" : 0, "stop_name" : 0, "next_stop" : 0, "stop_type" : 0, "a_time" : 0}
    # errors = {"stop_name" : 0, "stop_type" : 0, "a_time" : 0}
    # error_count = 0
    # a = 5
    result = {}
    # result1 = {a,}
    # print(type(result1))


    for data in json.loads(input()):
        if data["bus_id"] in result:
            result[data["bus_id"]].add(data["stop_id"])
        else:
            result.update({data["bus_id"] : {data["stop_id"],}})
        # if data["bus_id"] == None or not isinstance(data["bus_id"], int) or data["bus_id"] < 0:
        #     error_count += 1
        #     errors["bus_id"] += 1
        # if data["stop_id"] == None or not isinstance(data["stop_id"], int) or data["stop_id"] < 0:
        #     error_count += 1
        #     errors["stop_id"] += 1
        # if data["stop_name"] == None or not isinstance(data["stop_name"], str) or len(data["stop_name"]) == 0 or bad_name(data["stop_name"]):
        #     error_count += 1
        #     print("bad name:", data["stop_name"])
        #     errors["stop_name"] += 1
        # if data["next_stop"] == None or not isinstance(data["next_stop"], int) or data["next_stop"] < 0:
        #     error_count += 1
        #     errors["next_stop"] += 1
        # if data["stop_type"] != None and data["stop_type"] != "":
        #     if not isinstance(data["stop_type"], str) or len(data["stop_type"]) > 1 or not re.match("[SOF]", data["stop_type"]):
        #         error_count += 1
        #         errors["stop_type"] += 1
        # if data["a_time"] == None or not isinstance(data["a_time"], str) or not re.match("^([0-1][0-9]|2[0-3]):[0-5][0-9]$", data["a_time"]):
        #     error_count += 1
        #     errors["a_time"] += 1

    # print(MESSAGE.format(error_count))
    # for field in errors:
    #     # if errors[field] > 0:
    #         print(field, errors[field], sep=": ")

    print("Line names and number of stops:")
    for stop in result:
        print(f"bus_id: {stop}, stops: {len(result[stop])}")


if __name__ == "__main__":
    main()