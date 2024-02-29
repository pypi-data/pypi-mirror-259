from dataclasses import replace
from datetime import date, datetime


def dataclass(cls):
    from dataclasses import dataclass as dataclass_
    from functools import wraps

    @wraps(cls)
    def decorator(original_class):
        cls_dataclass_ = dataclass_(original_class)
        cls_dataclass_.__eq__ = cls_dataclass_.__eq2__
        cls_dataclass_.__hash__ = cls_dataclass_.__hash2__
        return cls_dataclass_

    return decorator(cls)
