#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    top_tup = ()
    bot_tup = ()
    if len(tuple_a) == len(tuple_b):
        top_tup = tuple_a
        bot_tup = tuple_b
    else:
        top_tup = tuple_a if len(tuple_a) > len(tuple_b) else tuple_b
        bot_tup = tuple_a if len(tuple_a) < len(tuple_b) else tuple_b
        for i in range(len(top_tup) - len(bot_tup)):
            bot_tup = bot_tup + (0,)
    res = []
    for i in range(0, len(top_tup)):
        res.append(top_tup[i] + bot_tup[i])
    res = tuple(res)
    return res
