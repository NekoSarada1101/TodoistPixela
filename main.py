from todoist.api import TodoistAPI
from datetime import datetime, timedelta
from settings_secret import *


def main():
    today = datetime.today()
    yesterday = (datetime(today.year, today.month, today.day, 0, 0, 0) - timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M")

    api = TodoistAPI(TODOIST_TOKEN)
    task = api.completed.get_all(since=yesterday)
    print(task)


if __name__ == "__main__":
    main()
