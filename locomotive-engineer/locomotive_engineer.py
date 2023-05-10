"""Functions which helps the locomotive engineer to keep track of the train."""
import copy


def get_list_of_wagons(*wagons_ids):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*wagons_ids]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    locomotive_wagon_id = each_wagons_id.index(1)
    return (
        [each_wagons_id[locomotive_wagon_id]]
        + missing_wagons
        + each_wagons_id[locomotive_wagon_id + 1 :]
        + each_wagons_id[:locomotive_wagon_id]
    )


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route = copy.deepcopy(route)
    route["stops"] = [value for value in stops.values()]
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    transposed_tuples = list(zip(*wagons_rows))
    return [list(sublist) for sublist in transposed_tuples]
