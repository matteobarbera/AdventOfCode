from collections import defaultdict
import numpy as np


def generate_fields(filename):
    fields = {}
    with open(filename) as f:
        for line in f:
            if (line := line.strip()) != "":
                k, v = line.split(":")
                k = k.replace(" ", "_")
                v1, v2 = [list(map(int, val.split("-"))) for val in v.split(" or ")]
                fields[k] = create_lambda(*v1, *v2)
            else:
                return fields


def create_lambda(v1_low, v1_high, v2_low, v2_high):
    return lambda x: (v1_low <= x <= v1_high) or (v2_low <= x <= v2_high)


def get_ticket(filename):
    with open(filename) as f:
        for line in f:
            if "your ticket" in line:
                return list(map(int, next(f).split(",")))


def get_nearby_tickets(filename):
    nearby_tickets_reached = False
    nearby_tickets = []
    with open(filename) as f:
        for line in f:
            if nearby_tickets_reached:
                nearby_tickets.append(list(map(int, line.split(","))))
            if "nearby" in line:
                nearby_tickets_reached = True
        return nearby_tickets


def get_valid_tickets(filename):
    fields = generate_fields(filename)
    valid_tickets = []
    for ticket in get_nearby_tickets(filename):
        for v in ticket:
            valid_arr = [field(v) for field in fields.values()]
            if not any(valid_arr):
                break
        else:
            valid_tickets.append(ticket)
    return valid_tickets


def day16_part1(filename):
    fields = generate_fields(filename)
    error_rate = 0
    for ticket in get_nearby_tickets(filename):
        for v in ticket:
            valid_arr = [field(v) for field in fields.values()]
            if not any(valid_arr):
                error_rate += v
    return error_rate


def day16_part2(filename):
    fields = generate_fields(filename)
    valid_tickets = get_valid_tickets(filename)
    my_ticket = get_ticket(filename)
    valid_tickets.append(my_ticket)

    ticket_dict = defaultdict(list)
    valid_tickets = np.asarray(valid_tickets)
    for f_name in fields.keys():
        for position, values in enumerate(valid_tickets.T):
            if not all([fields[f_name](v) for v in values]):
                continue
            else:
                ticket_dict[f_name].append(position)
    map_ticket_fields(ticket_dict)

    my_ticket_product = 1
    for f, p in ticket_dict.items():
        if "departure" in f:
            my_ticket_product *= my_ticket[p]
    return my_ticket_product


def map_ticket_fields(ticket_dict):
    n_fields = len(ticket_dict.keys())
    ctr = 0
    while ctr < n_fields:
        for f, ps in ticket_dict.items():
            if type(ps) == list and len(ps) == 1:
                position = ps[0]
                ticket_dict[f] = position
                ctr += 1
                for v in ticket_dict.values():
                    if type(v) == list:
                        v.remove(position)


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Ticket scanning error rate: {day16_part1('day16_input.txt')}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"My departure product: {day16_part2('day16_input.txt')}")
