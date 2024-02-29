from dataclasses import dataclass as dataclass_
from dataclasses import replace
from datetime import date, datetime


def dataclass(cls):
    cls = dataclass_(cls)
    cls.__eq__ = cls.__eq2__
    cls.__hash__ = cls.__hash2__
    return cls
