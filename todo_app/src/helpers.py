import itertools


def partition(predicate, iterable):
    """taken from the itertools recipe
    https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    t1, t2 = itertools.tee(iterable)
    return itertools.filterfalse(predicate, t1), filter(predicate, t2)
