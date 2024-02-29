"""
This file contains the attribute module

LICENSE: All rights reserved
"""
import inspect

from functools import wraps
from typing import Any, Callable

from Error import PrivateFunctionError


class private(object):
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if isinstance(func, type):
                # Classes
                if len(args) == 0:
                    raise PrivateFunctionError(f"You can not set a class as private if this class is not in another class")

                if args[0] is None or args[0].__class__.__name__ not in func.__qualname__.split("."):
                    raise PrivateFunctionError(f"Cannot call private class **{func.__name__}** directly from outside the class")
            else:
                # Functions
                if len(args) == 0:
                    raise PrivateFunctionError(f"You can not set a function as private if this function is not in a class")

                caller_frame = inspect.currentframe().f_back
                caller_locals = caller_frame.f_locals

                class_or_function_found = func.__globals__.get(func.__qualname__.split('.')[0])

                if args[0] is None or not isinstance(caller_locals.get("self"), args[0].__class__) or (not func.__globals__.get(
                        func.__qualname__.split('.')[0]) is args[0].__class__ and not class_or_function_found.__name__ == caller_locals.get("self").__class__.__name__):
                    raise PrivateFunctionError(f"Cannot call private function **{func.__name__}** directly from outside the class")

            try:
                return func(*args, **kwargs)
            except TypeError:
                return func()
        return wrapper


class fileprivate(object):
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            caller_frame = inspect.currentframe().f_back

            if isinstance(func, type):
                # Classes
                if inspect.getfile(func) != caller_frame.f_locals.get("__file__"):
                    raise PrivateFunctionError(f"Cannot call file private class **{func.__name__}** directly from outside the same file")
            else:
                # Functions
                if func.__code__.co_filename != caller_frame.f_code.co_filename:
                    raise PrivateFunctionError(f"Cannot call file private function **{func.__name__}** directly from outside the same file")
            try:
                return func(*args, **kwargs)
            except TypeError:
                return func()

        return wrapper


class protected(object):
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if len(args) == 0:
                raise PrivateFunctionError(f"You can not set a function as protected if this function is not in a class")

            caller_frame = inspect.currentframe().f_back
            caller_locals = caller_frame.f_locals

            if args[0] is None or not isinstance(caller_locals.get("self"), args[0].__class__):
                raise PrivateFunctionError(f"Cannot call protected function **{func.__name__}** directly from outside the class or the subclasses")
            return func(*args, **kwargs)

        return wrapper