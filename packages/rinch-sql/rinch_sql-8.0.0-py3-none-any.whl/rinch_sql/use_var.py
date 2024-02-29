from dataclasses import dataclass as dataclass_
from dataclasses import replace
from datetime import date, datetime


def dataclass(cls):
    def eq_method(self, other):
        if isinstance(other, cls):
            # 自定义的相等性比较逻辑
            return self.unique_key == other.unique_key
        return False

    cls = dataclass_(cls)
    cls.__eq__ = cls.__eq2__
    return cls
