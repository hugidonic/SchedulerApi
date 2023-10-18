from datetime import date, timedelta

import simplejson as json

def get_json(path: str):
    with open(path, encoding="utf8") as f:
        data = json.load(f)
        today = date.today()
        monday = today - timedelta(days=today.weekday())
        count = 0
        for scheduleDay in data:
            curDate = monday + timedelta(days=count)
            scheduleDay["date"] = curDate.strftime('%d.%m.%Y')
            count += 1
        return data