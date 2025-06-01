import pytest
from datetime import datetime
from src.cleaner import validate_logs, process_logs,LogEntry


def test_validate_logs_filters_invalid_entries():
    row_logs = [
        {"user_id": 1, "action": "play", "timestamp": "2024-05-01T09:00:00Z"},
        {"user_id": None, "action": "play", "timestamp": "2024-05-01T09:05:00Z"},
        {"user_id": 2, "action": "stop", "timestamp": "invalid-date"}
    ]
    valid = validate_logs(row_logs)
    assert len(valid) == 1
    assert valid[0].user_id == 1

def test_process_logs_computes_duration_correctly():
    logs = [
        LogEntry(user_id=1, action="play", timestamp=datetime.fromisoformat("2024-05-01T09:00:00")),
        LogEntry(user_id=1, action="pause", timestamp=datetime.fromisoformat("2024-05-01T09:15:00")),
    ]

    df = process_logs(logs)
    assert len(df) == 1
    assert df.iloc[0]["watch_duration"] == 900.0
    assert df.iloc[0]["user_id"] == 1

