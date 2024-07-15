#!/usr/bin/python

def parkingFee(hours):
    if hours <= 5:
        return hours * 1.0
    elif 5 < hours <=24:
        return 5 + (hours - 5) * 0.5
    elif hours == 24:
        return 15
    else:
        hours > 24
        return 15 + (hours - 24) * 0.5


print(parkingFee(26))
