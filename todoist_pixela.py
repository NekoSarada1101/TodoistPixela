import json
import requests
from todoist.api import TodoistAPI
from datetime import datetime, timedelta, timezone
from settings import *


def post_pixela():
    JST = timezone(timedelta(hours=+9), 'JST')  # type: timezone
    yesterday = (datetime.now(JST) - timedelta(days=1)).replace(hour=0, minute=0, second=0,
                                                                microsecond=0)  # type: datetime
    since = yesterday.replace(tzinfo=timezone.utc) - timedelta(hours=9)  # type: datetime
    print("yesterday=" + str(yesterday))
    print("since=" + str(since))

    api = TodoistAPI(TODOIST_TOKEN)  # type: TodoistAPI
    task = api.completed.get_all(since=since.strftime("%Y-%m-%dT%H:%M"))  # type: dict

    complete_task = str(len(task["items"]))  # type: str
    print("complete_task=" + complete_task)

    header = {"X-USER-TOKEN": PIXELA_TOKEN}  # type: dict
    payload = {"date": yesterday.strftime("%Y%m%d"), "quantity": complete_task}  # type: dict
    print("payload=" + str(payload))
    response = requests.post(PIXELA_URL, json.dumps(payload), headers=header)  # type: response
    print("response=" + response.text)
