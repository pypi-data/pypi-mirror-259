from contextlib import suppress
from datetime import datetime
from itertools import filterfalse, tee, zip_longest
from operator import methodcaller
from typing import Any, Iterable, List, Literal


class unset:
    pass


def identity(value: any):
    return value


def safe_int(val: Any, default=0, min_=None, max_=None) -> int:
    with suppress(Exception):
        val = int(val)
        if min_ is not None:
            val = max(val, min_)
        if max_ is not None:
            val = min(val, max_)
        return int(val)
    return default


def queryset_iterator(queryset, chunk_size: int = 1000):
    total = queryset.count()
    for start in range(0, total, chunk_size):
        end = min(start + chunk_size, total)
        yield queryset[start:end], start, end


def extract(params: dict, *keys, default: any = unset, how: Literal["get", "pop"] = "get") -> tuple:
    assert how in ["get", "pop"], f"how must be one of ['get', 'pop'], got {how}."

    if default is not unset:
        if not isinstance(default, (list, tuple, set)):
            default = [default] * len(keys)
        pairs = zip_longest(keys, default, fillvalue=None)
        return tuple(methodcaller(how, key, def_)(params) for key, def_ in pairs)
    return tuple(methodcaller(how, key)(params) for key in keys)


def deduplicate(seq: Iterable, key: callable = identity, keep: Literal["first", "last"] = "first") -> List:
    assert keep in ["first", "last"], f"keep must be one of ['first', 'last'], got {keep}."

    seen = {}
    for item in seq:
        k = key(item)
        if keep == "first" and k not in seen:
            seen[k] = item
        if keep == "last":
            seen[k] = item

    return list(seen.values())


def to_timestamp(dt, default=0, round_ts=False) -> int | float:
    if isinstance(dt, datetime):
        if round_ts:
            return round(dt.timestamp() * 1e3)
        return dt.timestamp()
    return default


def partition(iterable: Iterable, pred: callable = identity):
    t1, t2 = tee(iterable)
    return filter(pred, t1), filterfalse(pred, t2)
