import pytest

class TestValgrindParser(object):
    def test_trycatch_decorator(self):
        from src.decorators import trycatch
        @trycatch
        def func():
            a = []
            return a[2]  # Index error

        func()

    def test_timer_decorator(self):
        from src.decorators import timer
        @timer
        def func():
            pass

        func()

    def test_singleton_decorator(self):
        from src.decorators import singleton
        @singleton
        class A(object):
            def __init__(self, *args, **kwargs):
                pass

        obj1 = A(name='Siddhesh')
        obj2 = A(name='Siddhesh', lname='Sathe')
        obj3 = A(name='Siddhesh', lname='Sathe')
        assert obj1 is not obj2, "Created objects must be different"
        assert obj2 is obj3, "Created objects must be same"
