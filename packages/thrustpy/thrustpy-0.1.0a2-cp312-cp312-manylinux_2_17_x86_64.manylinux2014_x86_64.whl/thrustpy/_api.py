import _thrustpy


def add(arr1, arr2, out=None):
    return _thrustpy.add(arr1, arr2, out)


def subtract(arr1, arr2, out=None):
    return _thrustpy.subtract(arr1, arr2, out)


def divide(arr1, arr2, out=None):
    return _thrustpy.divide(arr1, arr2, out)


def floor_divide(arr1, arr2, out=None):
    return _thrustpy.floor_divide(arr1, arr2, out)


def true_divide(arr1, arr2, out=None):
    return _thrustpy.true_divide(arr1, arr2, out)


def multiply(arr1, arr2, out=None):
    return _thrustpy.multiply(arr1, arr2, out)


def array_sum(data):
    return _thrustpy.array_sum(data)


def sort(data):
    return _thrustpy.sort(data)


def strided_sort(data):
    return _thrustpy._strided_sort(data)
