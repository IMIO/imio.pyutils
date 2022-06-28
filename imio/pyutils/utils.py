# -*- coding: utf-8 -*-
#
# python utils methods
# IMIO <support@imio.be>
#

from collections import defaultdict
from collections import OrderedDict
from itertools import chain
from operator import methodcaller

import itertools
import time


def ftimed(f, nb=100, fmt='{:.7f}'):
    duration, ret = timed(f, nb=nb)
    return fmt.format(duration), ret


def get_clusters(numbers=[], separator=", "):
    """Return given p_numbers by clusters.
       When p_numbers=[1,2,3,5,6,8,9,10,15,17,20],
       the result is '1-3, 5-6, 8-10, 15, 17, 20'."""
    clusters = itertools.groupby(numbers, lambda n, c=itertools.count(): n-next(c))
    res = []
    for group, cluster in clusters:
        clust = list(cluster)
        if len(clust) > 1:
            res.append('{0}-{1}'.format(clust[0], clust[-1]))
        else:
            res.append('{0}'.format(clust[0]))
    return separator.join(res)


def insert_in_ordereddict(dic, value, after_key='', at_position=None):
    """Insert a tuple in an new Ordereddict.

        :param dic: the original OrderedDict
        :param value: a tuple (key, value) that will be added at correct position
        :param after_key: key name after which the tup is added
        :param at_position: position at which the tup is added. Is also a default if after_key is not found
        :return: a new OrderedDict or None if insertion position is undefined
    """
    position = None
    if after_key:
        position = odict_index(dic, after_key, delta=1)
    if position is None and at_position is not None:
        position = at_position
    if position is None:
        return None
    if position >= len(dic.keys()):
        return OrderedDict(list(dic.items()) + [value])
    tuples = []
    for i, tup in enumerate(dic.items()):
        if i == position:
            tuples.append(value)
        tuples.append(tup)
    if not tuples:  # dic was empty
        tuples.append(value)
    return OrderedDict(tuples)


def iterable_as_list_of_list(lst, cols=1):
    """Transform an iterable as list of list.

    :param lst: input iterable
    :param cols: number of columns in the sublists
    :return: list of lists
    """
    res = []
    sublist = []
    for i, item in enumerate(lst, start=1):
        sublist.append(item)
        if not i % cols:
            if sublist:
                res.append(sublist)
            sublist = []
    # put the last sublist in res
    if sublist:
        res.append(sublist)
    return res


def merge_dicts(dicts, as_dict=True):
    """Merge dicts, extending values of each dicts,
       useful for example when the value is a list.

    :param dicts: the list of dicts to mergeinput iterable
    :param as_dict: return a dict instead the defaultdict instance
    :return: a single dict (or defaultdict)
    """
    dd = defaultdict(list)

    # iterate dictionary items
    dict_items = map(methodcaller('items'), dicts)
    for k, v in chain.from_iterable(dict_items):
        dd[k].extend(v)
    return as_dict and dict(dd) or dd


def odict_index(odic, key, delta=0):
    """Get key position in an ordereddict"""
    for i, k in enumerate(odic):
        if k == key:
            return i + delta
    return None


def odict_pos_key(odic, pos):
    """Get key corresponding at position"""
    keys = [k for k in odic]
    if pos < 0:
        return None
    else:
        return keys[pos]


def replace_in_list(lst, value, replacement, generator=False):
    """
        Replace a value in a list of values.
        :param lst: the list containing value to replace
        :param value: the value to be replaced
        :param replacement: the new value to replace with
        :param generator: will return a generator instead a list when set to True
        :return: a new list/generator with replaced values
    """
    def _replacer(lst, value, replacement):
        new_lst = list(lst)
        for item in new_lst:
            if item == value:
                yield replacement
            else:
                yield item
    res = _replacer(lst, value, replacement)
    if not generator:
        res = list(res)
    return res


def safe_encode(value, encoding='utf-8'):
    """Converts a value to encoding, only when it is not already encoded."""
    if isinstance(value, unicode):
        return value.encode(encoding)
    return value


def timed(f, nb=100):
    start = time.time()
    for i in range(nb):
        ret = f()
    return (time.time() - start) / nb, ret  # difference of time is float
