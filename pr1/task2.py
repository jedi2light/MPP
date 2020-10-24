#!/usr/bin/env python3

import sys

CITIES = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 4, 'D': 6},
    'C': {'A': 4, 'B': 4, 'E': 6},
    'D': {'B': 6, 'E': 2},
    'E': {'C': 6, 'D': 2},
}


class Journey:

    src: str = ""
    dst: str = ""
    start_hour: int = 0
    finish_hour: int = 0
    available_places: list = []

    @staticmethod
    def register(src, dst, path, start_hour):
        """
        Will register a new Journey
        :param: src: str, source location
        :param: dst: str, destination location
        :param: path: tuple, points to be driven through
        :param: start_hour, int, when the driver starts its own Journey
        """
        
        finish_hour = start_hour

        try:
            for pidx, point in zip(range(len(path)-1), path):
                if point != dst:
                    p_next = path[pidx+1]
                    finish_hour += CITIES[point][p_next]
        except KeyError:
            raise Exception('Given path is invalid. Try again.' +
                    f'There is no way from {point} to {p_next}')

        return Journey(src, dst, path, start_hour, finish_hour)

    def __init__(self, src, dst, path, start_hour, finish_hour):
        """
        Will create a Juorney object
        :param: src: str, source location
        :param: dst: str, destination location
        :param: path: tuple, points to be driven through
        :param: start_hour, int, when a driver starts its own Journey
        :param: finish_hour: int, when a driver finishes its own Journey 
        """

        self.src = src
        self.dst = dst
        self.path = path
        self.start_hour = start_hour
        self.finish_hour = finish_hour

    @staticmethod
    def order(src, dst, journey_object):
        """
        Will return PlaceTicket object
        """

        return PlaceTicket((src, dst))

    @staticmethod
    def find(src, dst, journey_object_list):
        """
        Will return sufficient Journey object list
        """

        sufficient = []

        for jo in journey_object_list:
            if src in jo.path and dst in jo.path:
                sufficient.append(jo)

        return sufficient


class PlaceTicket:

    path: tuple = ()
    ordered: bool = False

    def __init__(self, path):
        """
        Will create a TicketPlace object
        """

        self.path = path


def main():

    # A driver can register a Journey like this:
    journey1 = Journey.register('A', 'D', ('A', 'C', 'B', 'D'), 8)
    journey2 = Journey.register('A', 'D', ('A', 'C', 'E', 'D'), 9)
    journey3 = Journey.register('A', 'D', ('A', 'B', 'D'), 10)
    
    registered_journeys = [journey1, journey2, journey3]

    # A passenger can find a sufficient Journey object list, simply path validation
    sufficient_journey_objects = Journey.find('A', 'B', registered_journeys)
    print(sufficient_journey_objects) # -> [journey1, journey3]
    
    # A passenger can order a sufficient Journey, without any validation yet
    place_ticket_object = Journey.order('A', 'B', journey1)
    print(place_ticket_object) # -> ...

    return 0
    

if __name__ == '__main__':

    sys.exit(main())
