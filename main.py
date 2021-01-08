import json
import requests
from todoist.api import TodoistAPI
from datetime import datetime, timedelta
from settings_secret import *


def main():
    today = datetime.today()  # type: datetime
    yesterday = (datetime(today.year, today.month, today.day, 0, 0, 0) - timedelta(hours=9)).strftime(
        "%Y-%m-%dT%H:%M")  # type: str

    api = TodoistAPI(TODOIST_TOKEN)  # type: TodoistAPI
    task = api.completed.get_all(since=yesterday)  # type: dict
    print("task=" + str(task))

    complete_task = str(len(task["items"]))  # type: str
    print("complete_task=" + complete_task)

    header = {"X-USER-TOKEN": PIXELA_TOKEN}  # type: dict
    payload = {"date": today.strftime("%Y%m%d"), "quantity": complete_task}  # type: dict
    print("payload=" + str(payload))
    response = requests.post(PIXELA_URL, json.dumps(payload), headers=header)  # type: response
    print("response=" + response.text)


if __name__ == "__main__":
    main()
