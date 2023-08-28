from fastapi import HTTPException

from api.helpers import get_date, get_json
from api.utils import week_day_names


async def get_schedule_for_date(date: str):
    date_val = get_date(date=date)

    #  Monday == 0 ... Sunday == 6.
    num_of_week = date_val.weekday()
    if num_of_week == 6:
        raise HTTPException(status_code=400, detail={
            "message": "No sunday in schedule"
        })

    day_of_week_name = week_day_names[num_of_week]
    return get_json("./api/json/chet/" + day_of_week_name + ".json")
