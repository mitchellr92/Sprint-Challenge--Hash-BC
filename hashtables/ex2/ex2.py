#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    print(length)
    for t in tickets:
        print(t.source, t.destination)
        hash_table_insert(hashtable, t.source, t.destination)

    print(route)

    key = "NONE"

    for i in range(length):
        current_ticket = hash_table_retrieve(hashtable, key)
        key = current_ticket
        # print(key)
        route[i] = current_ticket
        # print(route[i])

    print(route)

    return route
