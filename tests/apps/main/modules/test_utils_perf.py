import re
import time

import pytest

from src.apps.main.modules import utils_perf


def test_timer_registry_add_and_report():
    registry = utils_perf._TimerRegistry()

    registry.add("task_a", 0.1)
    registry.add("task_a", 0.2)
    registry.add("task_b", 0.05)

    count_a, total_a, max_a = registry.stats["task_a"]
    assert count_a == 2
    assert total_a == pytest.approx(0.3, rel=1e-6)
    assert max_a == 0.2

    count_b, total_b, max_b = registry.stats["task_b"]
    assert count_b == 1
    assert total_b == pytest.approx(0.05, rel=1e-6)
    assert max_b == 0.05

    report = registry.report()
    lines = report.splitlines()

    assert re.search(r"bloc.+calls.+total\(s\)", lines[0])

    task_lines = [line for line in lines if line.startswith("task_")]
    assert task_lines[0].startswith("task_a")
    assert task_lines[1].startswith("task_b")


def test_timeit_decorator_records_execution_time(monkeypatch):
    registry = utils_perf._TimerRegistry()
    monkeypatch.setattr(utils_perf, "TREG", registry)

    @utils_perf.timeit("sample_function")
    def sample_function(value):
        return value * 2

    assert sample_function(5) == 10

    count, total, max_dt = registry.stats["sample_function"]
    assert count == 1
    assert total >= 0
    assert max_dt >= 0


def test_time_block_records_elapsed_time(monkeypatch):
    registry = utils_perf._TimerRegistry()
    monkeypatch.setattr(utils_perf, "TREG", registry)

    with utils_perf.time_block("block_test"):
        time.sleep(0.001)

    count, total, max_dt = registry.stats["block_test"]
    assert count == 1
    assert total >= 0.001
    assert max_dt >= 0.001
