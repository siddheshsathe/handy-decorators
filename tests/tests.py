import io
import re
import time
import pytest
import typing
import logging
import threading
import contextlib


class TestValgrindParser(object):
    def test_trycatch_decorator(self, caplog: pytest.LogCaptureFixture) -> None:
        from src.decorators import trycatch

        @trycatch
        def func() -> object:
            a: list[object] = []
            return a[2]  # Index error

        with caplog.at_level(logging.INFO):
            result = func()

        assert len(caplog.records) == 1, "A single message must be logged"
        record = caplog.records[0]
        assert (
            record.message == "Exception occurred: [list index out of range]"
        ), "A message with the error must be logged"
        assert result is None, "The returned value must be None if there's error"

    def test_timer_decorator(self, caplog: pytest.LogCaptureFixture) -> None:
        from src.decorators import timer

        @timer
        def func() -> int:
            return 42

        with caplog.at_level(logging.INFO):
            result = func()

        pattern = re.compile(r"Time taken by the function is \[\d+\.\d+\] sec")
        assert len(caplog.records) == 1, "A single message must be logged"
        record = caplog.records[0]
        assert pattern.match(
            record.message
        ), "A message with the time taken must be logged"
        assert result == 42, "The returned value must be not None if it's the case"

    def test_singleton_decorator(self) -> None:
        from src.decorators import singleton

        @singleton
        class A(object):
            def __init__(self, *args, **kwargs) -> None:
                pass

        obj1: A = A(name="Siddhesh")
        obj2: A = A(name="Siddhesh", lname="Sathe")
        obj3: A = A(name="Siddhesh", lname="Sathe")
        assert obj1 is not obj2, "Created objects must be different"
        assert obj2 is obj3, "Created objects must be same"

    def test_run_in_thread(self, caplog: pytest.LogCaptureFixture) -> None:
        from src.decorators import run_in_thread

        @run_in_thread
        def display_1(*args, **kwargs) -> None:
            time.sleep(1)

        with caplog.at_level(logging.INFO):
            display_1()

        pattern = re.compile(r"Thread started for function <.+>")
        thread_pattern = re.compile(r"Thread-\d+ \(display_1\)")

        assert len(caplog.records) == 1, "A single message must be logged"
        for record in caplog.records:
            assert pattern.match(
                record.message
            ), "A message with the function must be logged"

        assert (
            sum(
                1
                for thread in threading.enumerate()
                if thread_pattern.match(thread.name)
            )
            == 1
        ), "A single thread must be created"

    def test_create_n_thread(self, caplog: pytest.LogCaptureFixture) -> None:
        from src.decorators import create_n_threads

        @create_n_threads(thread_count=2)
        def display_2(*args, **kwargs) -> None:
            time.sleep(1)

        with caplog.at_level(logging.INFO):
            display_2()

        pattern = re.compile(r"Thread started for function <.+>")
        thread_pattern = re.compile(r"Thread-(\d+) \(display_2\)")

        assert len(caplog.records) == 2, "Exactly two messages must be logged"
        for i, record in enumerate(caplog.records):
            assert pattern.match(
                record.message
            ), f"A message with the function must be logged at position {i}"

        assert (
            sum(
                1
                for thread in threading.enumerate()
                if thread_pattern.match(thread.name)
            )
            == 2
        ), "Exactly two threads must be created"
