# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - Intelligentica (Morocco)
Email: a.benmhamed@intelligentica.net
Website: https://intelligentica.net
"""


class Truck(object):
    """
    A class for creating a truck object

    :arg
    n (integer): the number of truck instances to create
    capacity (float): the capacity of the truck instance
    capacity_unit (str): the capacity unit for the truck (e.g. (kg), (t))
    avg_speed (float): the average speed of the truck
    max_speed (float): the max speed the truck can achieve or allowed to achieve
    min_speed (float): the min routing speed the truck can achieve or allowed to achieve
    speed_unit (str): the speed unit (e.g. (km/h), (m/h) (miles/h))
    """

    def __init__(self, n, capacity=None, capacity_unit="kg", avg_speed=None, max_speed=None, min_speed=None,
                 speed_unit="km/h"):

        if not isinstance(n, int):
            raise TypeError("'n' must be an integer")

        if not isinstance(capacity, float):
            raise TypeError("'capacity' must be a numeric")

        if capacity_unit not in ['kg', 't']:
            raise ValueError("'capacity_unit' must be 'kg', or 't'")

        if speed_unit not in ['km/h', 'miles/h', 'meters/h']:
            raise ValueError("'speed_unit' must be 'km/h', 'miles/h' or 'meters/h'")

        self.n = n
        self.capacity = capacity
        self.capacity_unit = capacity_unit
        self.avg_speed = avg_speed
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.speed_unit = speed_unit

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"\tn = {self.n}, \n" \
               f"\tcapacity = {self.capacity} ({self.capacity_unit}), \n" \
               f"\tavg_speed = {self.avg_speed} ({self.speed_unit}), \n" \
               f"\tmax_speed = {self.max_speed} ({self.speed_unit}), \n" \
               f"\tmin_speed = {self.min_speed} ({self.speed_unit})\n)"


class Drone(object):
    """
    A class for creating a drone object

    :arg
    n (integer): the number of truck instances to create
    capacity (float): the capacity of the truck instance
    capacity_unit (str): the capacity unit for the truck (e.g. (kg), (t))
    avg_speed (float): the average routing speed of the truck
    autonomy (float): the drone battery autonomy
    autonomy_unit (str): the autonomy unit (e.g (min), (hour))
    max_speed (float): the max routing speed the truck can achieve or allowed to achieve
    min_speed (float): the min routing speed the truck can achieve or allowed to achieve
    speed_unit (str): the speed unit (e.g. (km/h), (m/h) (miles/h))
    """

    def __init__(self, n, capacity, autonomy, avg_speed, max_speed=None, min_speed=None, capacity_unit="kg",
                 speed_unit="km/h", autonomy_unit="min"):

        if not isinstance(n, int):
            raise TypeError("'n' must be an integer")

        if not isinstance(capacity, float):
            raise TypeError("'capacity' must be a numeric")

        if capacity_unit not in ['kg', 't']:
            raise ValueError("'capacity_unit' must be 'kg', or 't'")

        if autonomy_unit not in ['min', 'hour']:
            raise ValueError("'autonomy_unit' must be 'min', or 'hour'")

        if speed_unit not in ['km/h', 'miles/h', 'meters/h']:
            raise ValueError("'speed_unit' must be 'km/h', 'miles/h' or 'meters/h'")

        self.n = n
        self.capacity = capacity
        self.autonomy = autonomy
        self.avg_speed = avg_speed
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.capacity_unit = capacity_unit
        self.speed_unit = speed_unit
        self.autonomy_unit = autonomy_unit

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"\tn = {self.n}, \n" \
               f"\tcapacity = {self.capacity} ({self.capacity_unit}), \n" \
               f"\tautonomy = {self.autonomy} ({self.autonomy_unit}), \n" \
               f"\tavg_speed = {self.avg_speed} ({self.speed_unit}), \n" \
               f"\tmax_speed = {self.max_speed} ({self.speed_unit}), \n" \
               f"\tmin_speed = {self.min_speed} ({self.speed_unit})\n)"
