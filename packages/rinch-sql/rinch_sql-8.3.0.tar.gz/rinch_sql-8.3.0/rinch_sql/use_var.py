from dataclasses import replace
from datetime import date, datetime


def dataclass(cls):
    from dataclasses import dataclass as dataclass_
    from functools import wraps

    @wraps(cls)
    @dataclass_
    class DecoratedClass(cls):
        def __hash__(self):
            return hash(tuple(self))

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return tuple(self) == tuple(other)
            else:
                return False

    return DecoratedClass
