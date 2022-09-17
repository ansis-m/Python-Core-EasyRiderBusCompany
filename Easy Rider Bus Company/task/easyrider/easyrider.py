import json
import re


def no_start_and_end(result):
    for line in result:
        if not result[line].issuperset({"S", "F"}):
            return line

    return "x"

def get_transfer_stops(transfers):
    result = []

    for stop in transfers:
        if len(transfers[stop]) > 1:
            result.append(stop)

    return result


def main():

    transfer_stops = ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
    terminals = {128 : {'Sesame Street', 'Prospekt Avenue'}, 256 : {'Pilotow Street', 'Sesame Street'}, 512 : {'Bourbon Street', 'Sunset Boulevard'}}


    start_stops = set() # all start stops
    finish_stops = set() # all finish stops
    transfers = {} # dict to find transfers
    result = {} # check if all lines have start and finish



    for data in json.loads(input()):
        if data["bus_id"] in result:
            result[data["bus_id"]].add(data["stop_type"])
        else:
            result.update({data["bus_id"] : {data["stop_type"],}})
        if data["stop_type"] == "S":
            start_stops.add(data["stop_name"])
        if data["stop_type"] == "F":
            finish_stops.add(data["stop_name"])
        if data["stop_name"] in transfers:
            transfers[data["stop_name"]].add(data["bus_id"])
        else:
            transfers.update({data["stop_name"] : {data["bus_id"],}})


    bad_line = no_start_and_end(result)
    if bad_line != "x":
        print("There is no start or end stop for the line: {}.".format(bad_line))
    else:
        start_stops = list(start_stops)
        start_stops.sort()
        print(f"Start stops: {len(start_stops)} {start_stops}")


        transfer_stops = get_transfer_stops(transfers)
        transfer_stops.sort()
        print(f"Transfer stops: {len(transfer_stops)} {transfer_stops}")

        finish_stops = list(finish_stops)
        finish_stops.sort()
        print(f"Finish stops: {len(finish_stops)} {finish_stops}")


if __name__ == "__main__":
    main()