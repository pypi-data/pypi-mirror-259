from dataclasses import replace
from datetime import date, datetime


def dataclass(cls):
    from dataclasses import dataclass as dataclass_
    from functools import wraps

    # 装饰器函数
    def decorator(original_class):
        # 保留原始签名
        @wraps(original_class)
        @dataclass_(eq=False)
        class DecoratedClass(original_class):
            def __hash2__(self):
                return hash(tuple(self))

            def __eq2__(self, other):
                if isinstance(other, self.__class__):
                    return tuple(self) == tuple(other)
                else:
                    return False

            def __iter__(self) -> iter:
                for i in self.field_list_unique:
                    value = self.__dict__[i]
                    yield value


        return DecoratedClass

    return decorator(cls)
