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

    for i in range(size):
        if i < size - 1 and list_of_integers[i] < list_of_integers[i+1]:
            mid = (mid + size) // 2
        elif i > 0 and list_of_integers[i] < list_of_integers[i-1]:
            mid = mid // 2
        else:
            return list_of_integers[mid]
