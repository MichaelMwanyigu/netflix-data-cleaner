import json
from datetime import datetime
from pydantic import BaseModel, ValidationError
import pandas as pd
from typing import List, Optional


class LogEntry(BaseModel):
    user_id: int
    action: str
    timestamp: datetime

def load_logs(filepath:str) -> List[dict]:
    with open(filepath, "r") as file:
        return json.load(file)

def validate_logs(row_logs: List[dict])-> List[LogEntry]:
    valid_entries = []
    for entry in row_logs:
        try:
            log = LogEntry(**entry)
            valid_entries.append(log)
        except ValidationError:
            continue
    return valid_entries

def process_logs(logs: List[LogEntry]) -> pd.DataFrame:
    data = [{"user_id": log.user_id, "action": log.action, "timestamp": log.timestamp} for log in logs]

    data_frame = pd.DataFrame(data)

    data_frame = data_frame.sort_values(by=["user_id","timestamp"])

    watch_times = []
    prev_action = {}

    for _, row in data_frame.iterrows():
        user_id = row["user_id"]
        action = row["action"]
        time = row["timestamp"]

        if action == "play":
            prev_action[user_id] = time

        elif action in ("pause", "stop") and user_id in prev_action:
            duration = (time - prev_action[user_id]).total_seconds()
            if 0 < duration < 36000:
                watch_times.append({"user_id":user_id, "watch_duration": duration})
            del prev_action[user_id]
    
    return pd.DataFrame(watch_times)

def save_to_csv(data_frame: pd.DataFrame,filepath: str):
    data_frame_grouped = data_frame.groupby("user_id").sum().reset_index()
    data_frame_grouped.to_csv(filepath,index=False)

def run_etl():
    row_logs =  load_logs("data/row_logs.json")
    valid_logs = validate_logs(row_logs)
    cleaned_data_frame = process_logs(valid_logs)
    save_to_csv(cleaned_data_frame, "output/watch_duration.csv")


if __name__ == "__main__":
    run_etl()



