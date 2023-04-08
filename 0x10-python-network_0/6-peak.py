#!/usr/bin/python3
""" Function finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers
    Return: the peak or None
    """
    size = len(list_of_integers)
    mid = size // 2

    if size == 0:
        return None

    while True:
        if mid > 0 and list_of_integers[mid-1] > list_of_integers[mid]:
            mid -= 1
        elif mid < size-1 and list_of_integers[mid+1] > list_of_integers[mid]:
            mid += 1
        else:
            return list_of_integers[mid]
