from fastapi import FastAPI, HTTPException
import simplejson as json
from datetime import datetime

app = FastAPI()
chet = "./api/json/chet/"
nechet = "./api/json/nechet/"

# https://www.kstu.ru/www_Ggrid.jsp?x=www_GFgrid&d=2022-11-09&f=210&g=34326#2022-11-09

week_day_names = [
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat",
]

types_of_week = [
    "chet",
    "nechet"
]

@app.get("/schedule")
async def get_schedule_for_date(date: str):
    try:
        date_val = datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        raise HTTPException(status_code=400, detail={
            "message": f"Bad date: {date}"
        })

    num_of_week = date_val.weekday()
    if num_of_week > 5:
        raise HTTPException(status_code=400, detail={
            "message": "No sunday in schedule"
        })

    day_of_week_name = week_day_names[num_of_week]

    return get_json("chet", day_of_week_name)


@app.get("/schedule/{type_of_week}/{day_of_week}")
async def get_schedule_for_day_of_week(type_of_week: str, day_of_week: str):
    if day_of_week not in week_day_names or type_of_week not in types_of_week:
        raise HTTPException(status_code=404, detail={
            "message": f"Bad data"
        })

    return get_json(type_of_week, day_of_week)


def get_json(type_of_week: str, day_of_week: str):
    with open("./api/json/" + type_of_week + "/" + day_of_week + ".json", encoding="utf8") as f:
        return json.load(f)


@app.get("/schedule/details")
def get_subject_details():
    return         {
            "title": "Информационные технологии в информационной безопасности",
            "shortTitle": "ИТВИБ",
            "type": "Лабораторная Работа",
            "prepod": "Богомолов В.А.",
            "cabinet": "П-7",
            "duration": "1 сен - 4 дек",
            "startTime": "9:40",
            "endTime": "11:10"
        },