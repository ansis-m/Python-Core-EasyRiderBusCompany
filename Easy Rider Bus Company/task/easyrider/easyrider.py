import json
import re


def no_start_and_end(result):
    for line in result:
        if not result[line].issuperset({"S", "F"}):
            return line

    return "x"

def get_transfer_stops(transfers):
    result = set()

    for stop in transfers:
        if len(transfers[stop]) > 1:
            result.add(stop)

    return result


def main():

    transfer_stops = ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
    terminals = {128 : {'Sesame Street', 'Prospekt Avenue'}, 256 : {'Pilotow Street', 'Sesame Street'}, 512 : {'Bourbon Street', 'Sunset Boulevard'}}


    start_stops = set() # all start stops
    finish_stops = set() # all finish stops
    ondemand_stops = set()
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
        if data["stop_type"] == "O":
            ondemand_stops.add(data["stop_name"])
        if data["stop_name"] in transfers:
            transfers[data["stop_name"]].add(data["bus_id"])
        else:
            transfers.update({data["stop_name"] : {data["bus_id"],}})


    transfer_stops = get_transfer_stops(transfers)

    bad_stops = []

    for stop in ondemand_stops:
        if stop in start_stops.union(finish_stops).union(transfer_stops):
            bad_stops.append(stop)


    print("On demand stops test:")
    if len(bad_stops) == 0:
        print("OK")
    else:
        bad_stops.sort()
        print("Wrong stop type:", bad_stops)


if __name__ == "__main__":
    main()