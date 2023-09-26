import pytest
import typing

class TestValgrindParser(object):
    def test_trycatch_decorator(self) -> None:
        from src.decorators import trycatch
        @trycatch
        def func() -> object:
            a: list[object] = []
            return a[2]  # Index error

        func()

    def test_timer_decorator(self) -> None:
        from src.decorators import timer
        @timer
        def func() -> None:
            pass

        func()

    def test_singleton_decorator(self) -> None:
        from src.decorators import singleton
        @singleton
        class A(object):
            def __init__(self, *args, **kwargs) -> None:
                pass

        obj1: A = A(name='Siddhesh')
        obj2: A = A(name='Siddhesh', lname='Sathe')
        obj3: A = A(name='Siddhesh', lname='Sathe')
        assert obj1 is not obj2, "Created objects must be different"
        assert obj2 is obj3, "Created objects must be same"

    def test_run_in_thread(self) -> None:
        from src.decorators import run_in_thread
        @run_in_thread
        def display(*args, **kwargs) -> None:
            pass
        display()

    def test_create_n_thread(self) -> None:
        from src.decorators import create_n_threads
        @create_n_threads(thread_count=2)
        def display(*args, **kwargs) -> None:
            pass
        display()
